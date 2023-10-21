from rest_framework.viewsets import ModelViewSet

from kids_shop.permissions import IsOwner
from users.serializers import ProfileSerializer
from users.users_repository import ProfileRepository


class ProfileViewSet(ModelViewSet):
    profile_repository = ProfileRepository()
    queryset = profile_repository.get_all_objects_order_by_id()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwner]
    http_method_names = ['get', 'patch']
