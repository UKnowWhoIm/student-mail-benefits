from rest_framework import viewsets
from rest_framework import mixins
from .permissions import IsAdminOrSafe
from django_filters import rest_framework as filters
from .serializers import BenefitSerializer, CategorySerializer
from .models import Benefit, Category


class BenefitView(viewsets.ModelViewSet):
    queryset = Benefit.objects.filter(is_verified=True)
    permission_classes = [IsAdminOrSafe]
    serializer_class = BenefitSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ["category"]


class CategoryViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
