from django.urls import path
from .web_views import new_benefit

urlpatterns = [
    path("new", new_benefit)
]
