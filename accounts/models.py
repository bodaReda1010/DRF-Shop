from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Profile(models.Model):
    name = models.OneToOneField(User , on_delete=models.CASCADE)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    phone = models.CharField(max_length=50)

    

    class Meta:
        verbose_name = ("Profile")
        verbose_name_plural = ("Profiles")

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(name=instance) 

    def __str__(self):
        return str(self.name)



@receiver(post_save , sender =settings.AUTH_USER_MODEL)
def token_create(sender , instance , created , **kwargs):
    if created:
        Token.objects.create(user = instance)


        