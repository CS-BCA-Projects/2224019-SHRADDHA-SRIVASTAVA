from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),  # Define the home page
    path('index/', views.index, name='About'),
    path("contact/", views.contact, name='contact'),
]

