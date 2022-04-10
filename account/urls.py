from django.urls import path
from . import views

app_name = "account"
urlpatterns = [
	path("register", views.RegistrationFormView.as_view(), name="register"),
	path("login", views.LoginFormView.as_view(), name="login"),
	path("logout", views.LogoutView.as_view(), name="logout"),
	path("profile", views.UpdateProfileFormView.as_view(), name="profile"),
	path("recipe/search", views.SearchAPIView.as_view(), name="search")
]