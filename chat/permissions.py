from rest_framework.permissions import BasePermission, IsAuthenticated

class IsOwnerAndAuthenticated(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_authenticated and obj.client == request.user