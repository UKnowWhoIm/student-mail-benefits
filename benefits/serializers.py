from rest_framework import serializers
from .models import Benefit, Category, Contribution


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BenefitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Benefit
        fields = "__all__"


class BenefitReadSerializer(BenefitSerializer):
    class Meta:
        model = Benefit
        fields = "__all__"
        depth = 1


class BenefitWriteSerializer(BenefitSerializer):
    email = serializers.EmailField(write_only=True, required=False, default=None)

    @staticmethod
    def clean(data):
        # Remove email and set category to id
        data = {key: val for key, val in data.items() if key != "email"}
        if data.get("category"):
            data["category"] = data["category"].id
        return data

    def create(self, validated_data):
        Contribution.objects.create(
            email=validated_data.get("email"),
            contribution=self.clean(validated_data),
            approved=self.context["request"].user.is_staff
        )

    def update(self, instance, validated_data):

        # Check for changes
        fields = [_.name for _ in Benefit._meta.fields]
        common_keys = set(fields).intersection(set(validated_data.keys()))
        if all([getattr(instance, key) == validated_data[key] for key in common_keys]):
            raise serializers.ValidationError("There are no new changes")

        Contribution.objects.create(
            email=validated_data.get("email"),
            contribution=self.clean(validated_data),
            benefit=self.instance,
            approved=self.context["request"].user.is_staff
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

    def validate_email(self, value):
        # Add email if staff user
        if self.context["request"].user.is_staff:
            return self.context["request"].user.email
        return value

