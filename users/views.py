from rest_framework.viewsets import ModelViewSet

from kids_shop.permissions import IsOwner
from users.serializers import CustomUserSerializer, ProfileSerializer
from users.users_repository import ProfileRepository, UserRepository

from urllib.parse import urlencode
from rest_framework import serializers
from rest_framework.views import APIView
from django.conf import settings
from django.shortcuts import redirect
from rest_framework.response import Response
from .mixins import PublicApiMixin, ApiErrorsMixin
from .utils import google_get_access_token, google_get_user_info, generate_tokens_for_user
from .models import CustomUser
from rest_framework import status
from .serializers import UserSerializer


class GoogleLoginApi(PublicApiMixin, ApiErrorsMixin, APIView):
    class InputSerializer(serializers.Serializer):
        code = serializers.CharField(required=False)
        error = serializers.CharField(required=False)

    def get(self, request, *args, **kwargs):
        input_serializer = self.InputSerializer(data=request.GET)
        input_serializer.is_valid(raise_exception=True)

        validated_data = input_serializer.validated_data

        code = validated_data.get('code')
        error = validated_data.get('error')

        login_url = f'{settings.BASE_FRONTEND_URL}'

        if error or not code:
            params = urlencode({'error': error})
            return redirect(f'{login_url}?{params}')

        redirect_uri = f'{settings.BASE_FRONTEND_URL}/google'
        access_token = google_get_access_token(code=code,
                                               redirect_uri=redirect_uri)

        user_data = google_get_user_info(access_token=access_token)

        try:
            user = CustomUser.objects.get(email=user_data['email'])
            access_token, refresh_token = generate_tokens_for_user(user)
            response_data = {
                'user': UserSerializer(user).data,
                'access_token': str(access_token),
                'refresh_token': str(refresh_token)
            }
            return Response(response_data, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            # username = user_data['email'].split('@')[0]
            first_name = user_data.get('given_name', '')
            last_name = user_data.get('family_name', '')

            user = CustomUser.objects.create(
                email=user_data['email'],
                first_name=first_name,
                last_name=last_name,
                registration_method='google'
            )

            access_token, refresh_token = generate_tokens_for_user(user)
            response_data = {
                'user': UserSerializer(user).data,
                'access_token': str(access_token),
                'refresh_token': str(refresh_token)
            }
            return Response(response_data, status=status.HTTP_200_OK)

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
