from django.views.generic import TemplateView


class HomeView(TemplateView):
	template_name = "app/index.html"


class AboutView(TemplateView):
	template_name = "app/about.html"
