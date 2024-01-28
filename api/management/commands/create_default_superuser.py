import typing as t

from django.core.management.base import BaseCommand

from kids_shop.settings import SUPER_LOGIN, SUPER_PASSWORD
from users.models import CustomUser


class Command(BaseCommand):
    help = 'Automatically creates a superuser if one does not exist'

    def handle(self, *args: t.Any, **options: t.Any) -> None:
        if not CustomUser.objects.filter(is_superuser=True).exists():
            CustomUser.objects.create_superuser(SUPER_LOGIN, SUPER_PASSWORD)
            self.stdout.write(
                self.style.SUCCESS('Superuser created successfully')
            )
        else:
            self.stdout.write(self.style.SUCCESS('Superuser already exists'))
