from django.urls import path
from . import views
from .views import HomeView


app_name = "app"
urlpatterns = [
	path("", HomeView.as_view(), name="home"),
    path("About-Us", views.about_us, name="about"),
    path("FAQs", views.faq_req, name="questions")


]


