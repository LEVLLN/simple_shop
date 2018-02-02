from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Content

# Create your views here.
class HomePageView(TemplateView):
	template_name = 'home.html'
	

class AboutPageView(TemplateView):
	template_name = 'about.html'
	
class BlogPageView(ListView):
	template_name = 'blog.html'
	model = Content

class BlogDetailView(DetailView):
	template_name = 'blog_detail.html'
	model = Content

class BlogCreateView(CreateView):
	template_name = 'blog_new.html'
	model = Content
	fields = '__all__'

class BlogUpdateView(UpdateView):
    model = Content
    fields = ['title', 'text', 'description']
    template_name = 'blog_edit.html'