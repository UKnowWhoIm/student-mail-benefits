from django.urls import path, include
from .views import BenefitView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'benefits', BenefitView)

urlpatterns = router.urls
