from django.urls import path
from .views import index, profile, logout

urlpatterns = [
    path('', index, name='index'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
]