from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import CustomUser, Profile


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, **kwargs):
    if not instance.is_superuser:
        if not hasattr(instance, 'users_profile'):
            user_profile = Profile(id=instance.id, user=instance)
            user_profile.save()
