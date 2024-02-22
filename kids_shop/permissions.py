from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view) -> bool:
        return bool(
            request.method in SAFE_METHODS or (request.user and request.user.is_staff)
        )


class IsOwner(BasePermission):

    def has_permission(self, request, view) -> bool:
        if request.user.is_authenticated or request.user.is_superuser:
            return True
        return request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj) -> bool:
        if request.user.is_authenticated and obj.user == request.user:
            return True
        return False


class IsOwnerFavoriteOrCart(BasePermission):
    def has_permission(self, request, view):
        profile_id = view.kwargs.get('profile_id')
        return request.user.is_authenticated and str(request.user.id) == profile_id
