from rest_framework import serializers
from .models import Benefit, Category
import json


class BenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefit
        exclude = ["is_verified"]

    def validate_highlights(self, value):
        try:
            obj = json.loads(value)
            if type(obj) != list:
                raise serializers.ValidationError("Highlights must Be JSON list")
        except json.JSONDecodeError:
            raise serializers.ValidationError("Invalid JSON")
        return value


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
