from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from api.models import Favorite
from api.serializers import FavoriteSerializer

from .models import CustomUser


class CustomUserCreateSerializer(UserCreateSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )

    def validate_password(self, value):
        return value

    class Meta:
        model = CustomUser
        fields = ('email', 'id', 'password', 'first_name', 'last_name')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
        )
        return user


class CustomUserSerializer(UserSerializer):
    favorite = FavoriteSerializer(many=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'id', 'first_name', 'last_name', 'favorite')
