from django.contrib.auth import get_user_model, login, authenticate
from django.shortcuts import render, redirect
from account.forms import RegistrationForm


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
			return redirect("home")
	else:
		form = RegistrationForm()
	return render(request, "account/register.html", {"form": form})
