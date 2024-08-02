from rest_framework.viewsets import ModelViewSet

from kids_shop.permissions import IsOwner
from users.serializers import (
    CustomUserSerializer,
    ProfileSerializer,
    AddressSerializer
)
from users.users_repository import (
    ProfileRepository,
    UserRepository,
    AddressRepository
)


class CustomUserView(ModelViewSet):
    user_repository = UserRepository()
    queryset = user_repository.get_all_objects_order_by_id()
    serializer_class = CustomUserSerializer
    permission_classes = [IsOwner]
    http_method_names = ['delete']


class ProfileViewSet(ModelViewSet):
    profile_repository = ProfileRepository()
    queryset = profile_repository.get_all_objects_order_by_id()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwner]
    http_method_names = ['get', 'patch']


class AddressViewSet(ModelViewSet):
    address_repository = AddressRepository()
    queryset = address_repository.get_all_objects_order_by_id()
    serializer_class = AddressSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
