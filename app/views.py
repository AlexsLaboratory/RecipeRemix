from django.shortcuts import render


# Create your views here.
def home_view(request):
	return render(request, "app/index.html")

def about_us(request):
	return render(request, "app/aboutUsPage.html")

