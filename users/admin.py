from django.contrib import admin
from django.contrib.auth.models import Group

from users.models import Address, CustomUser, Kid, Profile


class ProfileInline(admin.StackedInline):
    model = Profile


class KidInline(admin.StackedInline):
    model = Kid


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
    inlines = [ProfileInline]


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
    pass


admin.site.unregister(Group)
