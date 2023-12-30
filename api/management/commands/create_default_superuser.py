import typing as t

from django.core.management.base import BaseCommand

from users.models import CustomUser
from kids_shop.settings import SU_USER, SU_PASSWORD


class Command(BaseCommand):
    help = 'Automatically creates a superuser if one does not exist'

    def handle(self, *args: t.Any, **options: t.Any) -> None:
        if not CustomUser.objects.filter(is_superuser=True).exists():
            CustomUser.objects.create_superuser(SU_USER, SU_PASSWORD)
            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
        else:
            self.stdout.write(self.style.SUCCESS('Superuser already exists'))
