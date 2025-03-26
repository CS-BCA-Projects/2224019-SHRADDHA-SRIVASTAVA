from django.urls import path
from .views import questionnaire_view, dashboard_view

urlpatterns = [
    path('', questionnaire_view, name='questionnaire'),  # Form submission
    path('dashboard/<str:skin_type>/', dashboard_view, name='dashboard'),  # Redirect here
]


# from django.urls import path
# from .views import questionnaire_view, dashboard

# urlpatterns = [
#     path("questionnaire/", questionnaire_view, name="questionnaire"),
#     path("dashboard/<str:skin_type>", dashboard, name="dashboard"),
# ]
