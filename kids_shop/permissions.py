import os

from rest_framework.permissions import BasePermission

SAFE_METHODS = (
    os.environ.get('FIRST_METHOD'),
    os.environ.get('SECOND_METHOD'),
    os.environ.get('THIRD_METHOD'),
    os.environ.get('FOURTH_METHOD')
)


class IsAdminOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser == request.user:
            return True
        return request.method in SAFE_METHODS


class IsOwner(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser == request.user:
            return True
        return request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser or obj.user.id == request.user.id:
            return True
        return False
