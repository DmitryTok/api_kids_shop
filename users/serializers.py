from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework.serializers import EmailField, ModelSerializer
from rest_framework.validators import UniqueValidator

from users.models import Address, CustomUser, Kid, Profile


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
        fields = '__all__'


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


class ProfileSerializer(ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    address = AddressSerializer()
    kids = KidSerializer(many=True)

    class Meta:
        model = Profile
        fields = '__all__'

    def update(self, instance, validated_data):
        address_data = validated_data.pop('address', None)
        kids_data = validated_data.pop('kids', [])

        if not instance.address:
            instance.address = Address.objects.create()

        if address_data:
            instance.address.first_delivery_address = address_data.get('first_delivery_address',
                                                                       instance.address.first_delivery_address)
            instance.address.second_delivery_address = address_data.get('second_delivery_address',
                                                                        instance.address.second_delivery_address)
            instance.address.city = address_data.get('city', instance.address.city)
            instance.address.street = address_data.get('street', instance.address.street)
            instance.address.building = address_data.get('building', instance.address.building)
            instance.address.apartment = address_data.get('apartment', instance.address.apartment)
            instance.address.save()

        if kids_data:
            instance.kids.clear()
            for kid_data in kids_data:
                b_date = kid_data.get('birth_date')
                kid_male = kid_data.get('male')
                if b_date and kid_male:
                    kid, created = Kid.objects.get_or_create(male=kid_male, birth_date=b_date)
                    if not created:
                        for key, value in kid_data.items():
                            setattr(kid, key, value)
                        kid.save()
                else:
                    kid = Kid.objects.create(**kid_data)
                instance.kids.add(kid)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
