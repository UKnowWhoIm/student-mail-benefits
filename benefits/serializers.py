from rest_framework import serializers
from .models import Benefit


class BenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefit
        exclude = ["is_verified"]
