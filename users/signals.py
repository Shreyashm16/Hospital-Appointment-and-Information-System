from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import pat_Profile


@receiver(post_save, sender=User)
def create_pat_Profile(sender, instance, created, **kwargs):
    if created:
        pat_Profile(user=instance)


@receiver(post_save, sender=User)
def save_pat_Profile(sender, instance, **kwargs):
    instance.pat_Profile.save()
