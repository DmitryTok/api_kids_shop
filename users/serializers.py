from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from api.repository import ShoppingCartRepository
from users.models import CustomUser


class CustomUserCreateSerializer(UserCreateSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )

    class Meta:
        fields = (
            'email',
            'id',
            'password',
            'username',
            'first_name',
            'last_name'
        )
        model = CustomUser


class CustomUserSerializer(UserSerializer):

    class Meta:
        fields = (
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
        )
        model = CustomUser


class CustomUserShoppingCartSerializer(serializers.ModelSerializer):
    shoppingcart = serializers.StringRelatedField(many=True, read_only=True)
    total_count_products = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = (
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
            'shoppingcart',
            'total_count_products'
        )

    def get_total_count_products(self, obj):
        shoppingcart_repository = ShoppingCartRepository()
        request = self.context.get('request')
        if not request or request.user.is_anonymous:
            return False
        return shoppingcart_repository.get_all_users_products(request.user)
