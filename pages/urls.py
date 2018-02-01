from django.urls import path

from . import views

urlpatterns = [
	path('',views.HomePageView.as_view(),name="home"),
	path('about/',views.AboutPageView.as_view(),name="about"),
	path('blog/',views.BlogPageView.as_view(),name="blog"),
	path('blog/<int:pk>/', views.BlogDetailView.as_view(), name='content_detail'),
	path('blog/new/', views.BlogCreateView.as_view(), name='blog_new'),
]