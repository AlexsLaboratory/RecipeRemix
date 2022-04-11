from django.views.generic import TemplateView


class HomeView(TemplateView):
	template_name = "app/index.html"


class AboutView(TemplateView):
	template_name = "app/_aboutUsTemp.html"

class FaqView(TemplateView):
	template_name = "app/_FAQsPage.html"




class ProfileView(TemplateView):
	template_name = "app/profile.html"
