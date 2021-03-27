from .views import BenefitView, CategoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'benefits', BenefitView)
router.register(r'category', CategoryViewSet)

urlpatterns = router.urls
