from rest_framework.permissions import IsAdminUser, SAFE_METHODS


class IsAdminOrSafe(IsAdminUser):
    safe_methods = SAFE_METHODS + ("PATCH", "PUT")

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        return request.method in self.safe_methods or super().has_permission(request, view)
