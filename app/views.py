from django.views.generic import TemplateView


class HomeView(TemplateView):
	template_name = "app/index.html"


class AboutView(TemplateView):
	template_name = "app/about.html"


class FaqView(TemplateView):
	template_name = "app/FAQs.html"
	

class ProfileView(TemplateView):
	template_name = "app/profile.html"

	
class SearchView(TemplateView):
	template_name = "account/search.html"
