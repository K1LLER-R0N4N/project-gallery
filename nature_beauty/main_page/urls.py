from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('all_members/', views.all_members, name='All member'),
]
