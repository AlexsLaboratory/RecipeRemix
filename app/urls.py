from django.urls import path

from . import views
from .views import HomeView, AboutView, ProfileView, FaqView

app_name = "app"
urlpatterns = [
	path("", HomeView.as_view(), name="home"),
	path("FAQs", FaqView.as_view(), name="questions"),
	path("about", AboutView.as_view(), name="about"),
	path("profile", ProfileView.as_view(), name="profile")
]
