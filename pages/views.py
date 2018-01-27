from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Content

# Create your views here.
class HomePageView(ListView):
	template_name = 'home.html'
	model = Content

class AboutPageView(TemplateView):
	template_name = 'about.html'
	