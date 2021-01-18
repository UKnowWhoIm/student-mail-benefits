from rest_framework import serializers
from .models import Benefit, Category


class BenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefit
        exclude = ["is_verified"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
