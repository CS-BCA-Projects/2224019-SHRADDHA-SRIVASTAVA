from django.urls import path
from . import views

urlpatterns = [
    path('', views.custom_admin_dashboard, name='mongo_admin_home'),
    path("login/", views.custom_admin_login, name="custom_admin_login"),
    path("dashboard/", views.custom_admin_dashboard, name="admin_home"),  # ✅ FIXED
    path("logout/", views.custom_admin_logout, name="custom_admin_logout"),
    path("users/", views.user_list, name="user_list"),
    path("users/delete/<str:user_id>/", views.delete_user, name="delete_user"),
    path("contacts/", views.contact_list, name="contact_list"),
    path("contacts/delete/<str:contact_id>/", views.delete_contact, name="delete_contact"),
]

