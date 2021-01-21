from rest_framework import serializers
from .models import Benefit, Category


class BenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefit
        exclude = ["is_verified"]

    def validate_highlights(self, value):
        if type(value) != list:
            raise serializers.ValidationError("Highlights must Be JSON list")
        return value


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
