from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Perform actions after user is created"""
    if created:
        # Add any post-creation logic here
        print(f"New user created: {instance.username} with role: {instance.role}")user_model

User = get_user_model()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Perform actions after user is created"""
    if created:
        # Add any post-creation logic here
        print(f"New user created: {instance.username} with role: {instance.role}")