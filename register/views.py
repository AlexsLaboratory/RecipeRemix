from django.contrib.auth import get_user_model, login
from django.shortcuts import render, redirect
from .forms import RegisterForm

User = get_user_model()


# Create your views here.
def register(request):
	form = RegisterForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		email = form.cleaned_data.get("email")
		password = form.cleaned_data.get("password")
		password2 = form.cleaned_data.get("password_confirm")
		try:
			user = User.objects.create_user(username, email, password)
		except:
			user = None
		if user != None:
			login(request, user)
			return redirect("/")
		else:
			request.session['register_error'] = 1
	return render(request, "register/register.html", {"form": form})
