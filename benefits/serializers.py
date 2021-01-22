import json

from rest_framework import serializers
from .models import Benefit, Category, Contribution


class BenefitSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True, required=False, default=None)

    class Meta:
        model = Benefit
        fields = "__all__"

    @staticmethod
    def clean(data):
        data = {key: val for key, val in data.items() if key != "email"}
        if data.get("category"):
            data["category"] = data["category"].id
        return data

    def create(self, validated_data):
        approved = False
        if self.context["request"].user:
            # Approve changes if staff user is logged in
            approved = self.context["request"].user.is_staff
        Contribution.objects.create(
            email=validated_data.get("email"),
            contribution=self.clean(validated_data),
            approved=approved
        )

    def update(self, instance, validated_data):
        approved = False
        if self.context["request"].user:
            # Approve changes if staff user is logged in
            approved = self.context["request"].user.is_staff
        Contribution.objects.create(
            email=validated_data.get("email"),
            contribution=self.clean(validated_data),
            benefit=self.instance,
            approved=approved
        )

    def save(self, **kwargs):
        validated_data = {**self.validated_data, **kwargs}

        if self.instance is not None:
            self.update(self.instance, validated_data)
        else:
            self.create(validated_data)

    def validate_highlights(self, value):
        if type(value) != list:
            raise serializers.ValidationError("Highlights must Be JSON list")
        return value


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
