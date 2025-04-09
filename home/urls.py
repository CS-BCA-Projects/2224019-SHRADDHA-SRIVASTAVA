from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('booklet/', views.booklet_view, name='booklet'),
    path('fun-activity/', views.fun_activity, name='fun_activity'),
    path('relaxing-games/', views.relaxing_games, name='relaxing_games'),
]




# from django.contrib import admin
# from django.urls import path
# from home import views

# urlpatterns = [
#     path('', views.index, name='home'),  # Define the home page
#     path('index/', views.index, name='About'),
#     path("contact/", views.contact, name='contact'),
# ]

