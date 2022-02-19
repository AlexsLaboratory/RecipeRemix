from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

Account = get_user_model()


class RegistrationForm(UserCreationForm):
	username = forms.CharField(
		label="Username",
		widget=forms.TextInput(
			attrs={"class": "form-control", "name": "username"}
		)
	)
	email = forms.EmailField(
		label="Email",
		max_length=60,
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
		qs = Account.objects.filter(username__iexact=username)
		if qs.exists():
			raise forms.ValidationError("This is an invalid username, please pick another one.")
		return username

	def clean_email(self):
		email = self.cleaned_data.get("email")
		qs = Account.objects.filter(email__iexact=email)
		if qs.exists():
			raise forms.ValidationError("This email is already in use.")
		return email

	class Meta(UserCreationForm.Meta):
		model = Account
		fields = ("username", "email", "password1", "password2")
