from django.contrib.auth import get_user_model, login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from account.forms import RegistrationForm, AccountAuthenticationForm, AllergyUpdateForm


# Create your views here.
def registration_view(request):
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get("email")
			raw_password = form.cleaned_data.get("password1")
			account = authenticate(email=email, password=raw_password)
			login(request, account)
			return redirect("app:home")
		else:
			context["form"] = form
	else:
		context["form"] = RegistrationForm()
	return render(request, "account/register.html", context)


def logout_view(request):
	logout(request)
	return redirect("app:home")


def login_view(request):
	context = {}

	user = request.user
	if user.is_authenticated:
		return redirect("app:home")

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data.get("email")
			password = form.cleaned_data.get("password")
			user = authenticate(email=email, password=password)

			if user:
				login(request, user)
				return redirect("app:home")
	else:
		form = AccountAuthenticationForm()

	context["form"] = form
	return render(request, "account/login.html", context)


@login_required
def update_profile_view(request):
	context = {}
	if request.POST:
		form = AllergyUpdateForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.account = request.user
			instance.save()
	else:
		form = AllergyUpdateForm()
	context["form"] = form

	return render(request, "account/profile.html", context)
