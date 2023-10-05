from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework.serializers import EmailField, ModelSerializer
from rest_framework.validators import UniqueValidator

from users.models import Address, CustomUser, Kid


class CustomUserCreateSerializer(UserCreateSerializer):
    email = EmailField(
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )

    def validate_password(self, value):
        return value

    class Meta:
        model = CustomUser
        fields = ('email', 'id', 'password')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user


class CustomUserSerializer(UserSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'email')


class KidSerializer(ModelSerializer):
    class Meta:
        model = Kid
        fields = ('id', 'male', 'birth_date')


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = (
            'id',
            'first_delivery_address',
            'second_delivery_address',
            'city',
            'street',
            'building',
            'apartment'
        )

# TODO Create Profile serializer
