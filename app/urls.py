from django.urls import path
from .views import HomeView, AboutView, SearchView

app_name = "app"
urlpatterns = [
	path("", HomeView.as_view(), name="home"),
	path("about", AboutView.as_view(), name="about"),
	path("search", SearchView.as_view(), name="search")
]
