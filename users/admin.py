from django.contrib import admin
from django.contrib.auth.models import Group

from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name')
    search_fields = ('id', 'email', 'first_name', 'last_name')
    list_filter = ('id', 'email', 'first_name', 'last_name')
    exclude = [
        'date_joined',
        'last_login',
        'groups',
    ]


admin.site.unregister(Group)
