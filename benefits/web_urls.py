from django.urls import path
from .web_views import new_benefit, edit_benefit

urlpatterns = [
    path("new", new_benefit),
    path("edit", edit_benefit),
    path("edit/<int:benefit_id>", edit_benefit)
]
