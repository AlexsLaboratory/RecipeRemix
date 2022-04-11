from django.views.generic import TemplateView


class HomeView(TemplateView):
	template_name = "app/index.html"


class AboutView(TemplateView):
	template_name = "app/about.html"

def faq_req(request):
	return render(request, "app/_FAQsPage.html")


class ProfileView(TemplateView):
	template_name = "app/profile.html"
