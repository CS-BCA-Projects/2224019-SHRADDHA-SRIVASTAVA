from django.urls import path
from .views import register, dashboard, logout_view, login_view


urlpatterns = [
    # path("", index, name="index"),
    path("login/", login_view, name="login"),
    path("register/", register, name="register"),
    path("dashboard/<str:phone>/", dashboard, name="dashboard"),
    path("logout/", logout_view, name="logout"),
]

