from django.urls import path
from . import views

app_name = "account"
urlpatterns = [
	path("register", views.RegistrationFormView.as_view(), name="register"),
	path("login", views.LoginFormView.as_view(), name="login"),
	path("logout", views.LogoutView.as_view(), name="logout"),
	path("allergies", views.UpdateAllergiesFormView.as_view(), name="allergies"),
	path("pantry", views.UpdatePantryFormView.as_view(), name="pantry"),
	path("recipe/search", views.SearchAPIView.as_view(), name="search")
]