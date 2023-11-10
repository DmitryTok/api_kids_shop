from rest_framework.viewsets import ModelViewSet

from kids_shop.permissions import IsOwner
from users.serializers import CustomUserSerializer, ProfileSerializer
from users.users_repository import ProfileRepository, UserRepository


class CustomUserView(ModelViewSet):
    user_repository = UserRepository()
    queryset = user_repository.get_all_objects_order_by_id()
    serializer_class = CustomUserSerializer
    permission_classes = [IsOwner]
    http_method_names = ['delete']
    # def destroy(self, request, pk=None):
    #     try:
    #         user = CustomUser.objects.get(pk=pk)
    #     except CustomUser.DoesNotExist:
    #         return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
    #
    #     if user.id == request.user.id:
    #         user.delete()
    #     else:
    #         return Response({'detail': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
    #
    #     return Response({'detail': 'User deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)


class ProfileViewSet(ModelViewSet):
    profile_repository = ProfileRepository()
    queryset = profile_repository.get_all_objects_order_by_id()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwner]
    http_method_names = ['get', 'patch']
