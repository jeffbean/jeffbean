# coding=utf-8
# Create your models here.
from django.contrib.auth import get_user_model
from django.db import models
#from rest_framework.authtoken.models import Token


class AccountProfile(models.Model):
    user = models.OneToOneField(get_user_model())
    pagenation = models.BooleanField(default=True)
    save_search = models.BooleanField(default=True)

    class Meta:
        pass

    class Admin:
        fields = (
            ('Profile', {'fields': ('user', 'pagenation', 'save_search', 'product')}),
        )
        list_display = ('user',)


#@receiver(post_save, sender=get_user_model())
#def create_auth_token(sender, instance=None, created=False, **kwargs):
#    if created:
#        Token.objects.create(user=instance)