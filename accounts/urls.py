from django.urls import path
from .views import register, logout_view, login_view

urlpatterns = [
    path("login/", login_view, name="login"),
    path("register/", register, name="register"),
    path("logout/", logout_view, name="logout"),
]



# from django.urls import path
# from .views import register, logout_view, login_view


# urlpatterns = [
#     # path("", index, name="index"),
#     path("login/", login_view, name="login"),
#     path("register/", register, name="register"),
#     # path("dashboard/", dashboard, name="dashboard"),
#     path("logout/", logout_view, name="logout"),
# ]

