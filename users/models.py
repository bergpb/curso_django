from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    # on remove one user or user profile remove relation
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfis'

    def __str__(self):
        return '{} Profile'.format(self.user.username)
