from rest_framework.permissions import IsAdminUser, SAFE_METHODS


class UpdateBenefit(IsAdminUser):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS or super().has_permission(request, view)
