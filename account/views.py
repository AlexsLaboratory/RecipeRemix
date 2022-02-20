from django.contrib.auth import get_user_model, login, authenticate, logout
from django.shortcuts import render, redirect
from account.forms import RegistrationForm, AccountAuthenticationForm


# Create your views here.
def registration_view(request):
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get("username")
			email = form.cleaned_data.get("email")
			raw_password = form.cleaned_data.get("password")
			account = authenticate(email=email, password=raw_password)
			login(request, account)
			return redirect("app:home")
	else:
		form = RegistrationForm()
	return render(request, "account/register.html", {"form": form})


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
