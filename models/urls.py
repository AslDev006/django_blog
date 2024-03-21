from django.urls import path
from .views import *

urlpatterns = [
    path('home/', HomePageView, name='home_page'),
    path('about/', AboutPageView, name='about_page'),
    path('blog/', BlogPageView, name='blog_page'),
    path('contact/', ContactPageView, name='contact_page'),
    path('blog/<slug:slug>/', SinglePageView, name='single_page'),
]