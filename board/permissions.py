from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS or obj.user == request.user

class IsManagerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'DELETE':
            return request.user.is_authenticated and request.user.is_manager
        return True