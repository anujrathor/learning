from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        from django.db.models.signals import post_save
        from accounts.signals import create_user_profile
        from django.contrib.auth.models import User
        post_save.connect(create_user_profile, sender=User, dispatch_uid='create_user_profile')
