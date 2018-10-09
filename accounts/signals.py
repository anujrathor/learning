from django.db.models.signals import post_save
from django.contrib.auth.models import User
from accounts.models import Profile
from django.dispatch import receiver

@receiver(post_save,sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    Profile.objects.create(user=instance)
    Profile.save()


