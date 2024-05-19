from rest_framework.permissions import BasePermission


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        if obj.author == request.user or request.user.is_staff:
            return True
        return False


class IsAdminOrAuthent(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['POST', 'GET']:
            return request.user.is_authenticated
        return request.user and (
            request.user.is_staff or request.user.is_superuser)
