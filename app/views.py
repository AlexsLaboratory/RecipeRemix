from django.views.generic import TemplateView
from django.shortcuts import render

class HomeView(TemplateView):
	template_name = "app/index.html"

def about_us(request):
	return render(request, "app/aboutUsPage.html")

