from django.contrib import admin
from django.contrib.auth.models import Group

from users.models import Address, CustomUser, Kid, Profile


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
    search_fields = ('id', 'email')
    list_filter = ('id', 'email')
    exclude = [
        'first_name',
        'last_name',
        'date_joined',
        'last_login',
        'groups',
    ]


@admin.register(Kid)
class KidAdmin(admin.ModelAdmin):
    list_display = ('id', 'male', 'birth_date')
    search_fields = ('id', 'male', 'birth_date')
    list_filter = ('id', 'male', 'birth_date')


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_delivery_address',
        'second_delivery_address',
        'city',
        'street',
        'building',
        'apartment'
    )
    search_fields = (
        'id',
        'first_delivery_address',
        'second_delivery_address',
        'city',
        'street',
        'building',
        'apartment'
    )
    list_filter = (
        'id',
        'first_delivery_address',
        'second_delivery_address',
        'city',
        'street',
        'building',
        'apartment'
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'address',
        'kid',
        'first_name',
        'middle_name',
        'last_name',
        'birth_date',
        'first_phone',
        'second_phone'
    )
    search_fields = (
        'id',
        'user',
        'address',
        'kid',
        'first_name',
        'middle_name',
        'last_name',
        'birth_date',
        'first_phone',
        'second_phone'
    )
    list_filter = (
        'id',
        'user',
        'address',
        'kid',
        'first_name',
        'middle_name',
        'last_name',
        'birth_date',
        'first_phone',
        'second_phone'
    )


admin.site.unregister(Group)
