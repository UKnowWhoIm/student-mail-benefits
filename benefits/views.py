from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BenefitSerializer
from .models import Benefit


class BenefitView(viewsets.ModelViewSet):
    queryset = Benefit.objects.all()
    serializer_class = BenefitSerializer
