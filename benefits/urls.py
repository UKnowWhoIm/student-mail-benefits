from django.urls import path, include
from .views import BenefitView
from rest_framework.routers import DefaultRouter


#Creating router and registering viewsets
router = DefaultRouter()
router.register(r'benefits', BenefitView)

urlpatterns = [
    path('', include(router.urls))
]
