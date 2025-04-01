# period_tracker/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('track/', views.tracker_form, name='tracker_form'),
]