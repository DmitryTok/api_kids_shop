from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import Address, CustomUser, Kid, Profile


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, **kwargs):
    if not instance.is_superuser:
        if not hasattr(instance, 'users_profile'):
            user_profile = Profile(
                id=instance.id,
                user=instance
            )
            user_profile.save()


@receiver(post_save, sender=Profile)
def create_related_models(sender, instance, created, **kwargs):
    if created:
        kid = Kid.objects.create(male='Boy', birth_date=None)

        address = Address.objects.create(
            first_delivery_address='Your Address Here',
            second_delivery_address='Optional Address',
            city='Your City',
            street='Your Street',
            building='Your Building',
            apartment=1
        )

        instance.kids.add(kid)
        instance.address = address
        instance.save()
