from rest_framework import viewsets
from .permissions import UpdateBenefit
from .serializers import BenefitSerializer
from .models import Benefit


class BenefitView(viewsets.ModelViewSet):
    queryset = Benefit.objects.filter(is_verified=True)
    permission_classes = [UpdateBenefit]
    serializer_class = BenefitSerializer
