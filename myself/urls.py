from django.urls import path
from .views import profile_view, edit_profile, delete_profile

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('delete_profile/', delete_profile, name='delete_profile'),
]