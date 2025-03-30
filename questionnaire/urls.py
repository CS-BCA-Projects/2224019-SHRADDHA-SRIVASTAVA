from django.urls import path
from .views import questionnaire, dashboard

urlpatterns = [
    path('', questionnaire, name='questionnaire'),  # Form submission
    path('dashboard/<str:skin_type>/', dashboard, name='dashboard'),  # Redirect here
]


# from django.urls import path
# from .views import questionnaire_view, dashboard

# urlpatterns = [
#     path("questionnaire/", questionnaire_view, name="questionnaire"),
#     path("dashboard/<str:skin_type>", dashboard, name="dashboard"),
# ]
