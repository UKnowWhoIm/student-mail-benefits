from django.shortcuts import render
from rest_framework import generics
from .serializers import BenefitSerializer
from .models import Benefit


class BenefitView(generics.ListAPIView):
    queryset = Benefit.objects.all()
    serializer_class = BenefitSerializer
