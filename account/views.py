from django.contrib.auth import get_user_model, login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, CreateView
from django.views.generic.detail import SingleObjectMixin

from account.forms import RegistrationForm, AccountAuthenticationForm, AllergyUpdateForm, \
	AllergyUpdateFormSet, PantryUpdateForm, PantryUpdateFormSet
from account.models import Allergy, Pantry


class RegistrationFormView(FormView):
	form_class = RegistrationForm
	template_name = "account/register.html"
	success_url = reverse_lazy("app:home")

	def form_valid(self, form):
		form.save()
		email = form.cleaned_data.get("email")
		raw_password = form.cleaned_data.get("password1")
		account = authenticate(email=email, password=raw_password)
		login(self.request, account)
		return super().form_valid(form)


class LogoutView(View):
	def get(self, request):
		logout(request)
		return redirect("app:home")


class LoginFormView(FormView):
	form_class = AccountAuthenticationForm
	template_name = "account/login.html"
	success_url = reverse_lazy("app:home")

	def form_valid(self, form):
		email = form.cleaned_data.get("email")
		password = form.cleaned_data.get("password")
		user = authenticate(email=email, password=password)

		if user:
			login(self.request, user)
			return redirect("app:home")

		return super().form_valid(form)


class UpdateAllergiesFormView(LoginRequiredMixin, CreateView):
	model = Allergy
	template_name = "account/allergies.html"
	context_object_name = "formset"
	form_class = AllergyUpdateForm
	success_url = reverse_lazy("app:home")



	def post(self, request, *args, **kwargs):
		self.object = None
		formset = AllergyUpdateFormSet(request.POST)
		if formset.is_valid():
			return self.form_valid(formset)
		else:
			return self.form_invalid(formset)

	def get(self, request, *args, **kwargs):
		self.object = None
		allergy_form = AllergyUpdateFormSet(
			queryset=Allergy.objects.all().filter(account_id__exact=request.user.pk)
		)
		return self.render_to_response(self.get_context_data(formset=allergy_form))

	def form_valid(self, formset):
		if formset.deleted_forms:
			formset.save()
		else:
			for form in formset:
				child = form.save(commit=False)
				child.account = self.request.user
				child.save()
		return redirect("app:profile")

	def form_invalid(self, formset):
		return self.render_to_response(
			self.get_context_data(formset=formset)
		)


class UpdatePantryFormView(LoginRequiredMixin, CreateView):
	model = Pantry
	template_name = "account/pantry.html"
	context_object_name = "formset"
	form_class = PantryUpdateForm
	success_url = reverse_lazy("app:profile")

	def post(self, request, *args, **kwargs):
		self.object = None
		formset = PantryUpdateFormSet(request.POST)
		if formset.is_valid():
			return self.form_valid(formset)
		else:
			return self.form_invalid(formset)

	def get(self, request, *args, **kwargs):
		self.object = None
		pantry_form = PantryUpdateFormSet(
			queryset=Pantry.objects.all().filter(account_id__exact=request.user.pk)
		)
		return self.render_to_response(self.get_context_data(formset=pantry_form))

	def form_valid(self, formset):
		if formset.deleted_forms:
			formset.save()
		else:
			for form in formset:
				child = form.save(commit=False)
				child.account = self.request.user
				child.save()
		return redirect("app:profile")

	def form_invalid(self, formset):
		return self.render_to_response(
			self.get_context_data(formset=formset)
		)
