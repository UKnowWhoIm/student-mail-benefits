from rest_framework import viewsets, mixins
from rest_framework.filters import SearchFilter
from rest_framework.permissions import SAFE_METHODS
from .permissions import IsAdminOrSafe
from django_filters import rest_framework as filters
from .serializers import CategorySerializer, BenefitReadSerializer, BenefitWriteSerializer
from .models import Benefit, Category


class BenefitView(viewsets.ModelViewSet):
    queryset = Benefit.objects.all()
    permission_classes = [IsAdminOrSafe]
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)
    filterset_fields = ["category"]
    search_fields = ["title"]

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return BenefitReadSerializer
        return BenefitWriteSerializer


class CategoryViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
