from django.urls import path
from .views import HomeView, AboutView, ProfileView

app_name = "app"
urlpatterns = [
	path("", HomeView.as_view(), name="home"),
    path("About-Us", views.about_us, name="about"),
    path("FAQs", views.faq_req, name="questions")


	path("about", AboutView.as_view(), name="about"),
	path("profile", ProfileView.as_view(), name="profile")
]
