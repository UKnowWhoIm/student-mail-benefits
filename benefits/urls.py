from django.urls import path
from .views import BenefitView


urlpatterns = [
    path('benefits', BenefitView.as_view()),
]
