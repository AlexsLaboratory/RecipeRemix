from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
	username = forms.CharField(
		label="Username",
		widget=forms.TextInput(
			attrs={"class": "form-control", "name": "username"}
		)
	)
	email = forms.EmailField(
		label="Email",
		widget=forms.EmailInput(
			attrs={"class": "form-control", "name": "email"}
		)
	)
	password1 = forms.CharField(
		label="Password",
		widget=forms.PasswordInput(
			attrs={"class": "form-control", "name": "password"}
		)
	)
	password2 = forms.CharField(
		label="Password Confirm",
		widget=forms.PasswordInput(
			attrs={"class": "form-control", "name": "password-confirm"}
		)
	)

	def clean_username(self):
		username = self.cleaned_data.get("username")
		qs = User.objects.filter(username__iexact=username)
		if qs.exists():
			raise forms.ValidationError("This is an invalid username, please pick another one.")
		return username

	def clean_email(self):
		email = self.cleaned_data.get("email")
		qs = User.objects.filter(email__iexact=email)
		if qs.exists():
			raise forms.ValidationError("This email is already in use.")
		return email

	class Meta(UserCreationForm.Meta):
		model = User
		fields = ("username", "email", "password1", "password2")
