from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from dj_app.managers import CustomUserManager


class User(AbstractUser):

    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        app_label = "dj_app"
        verbose_name = "Nutzer"
        verbose_name_plural = "Nutzer"

    objects = CustomUserManager()

    def full_name(self, obj):
        return "{} {}".format(obj.first_name, obj.last_name)

    def __str__(self):
        return self.email

    @property
    def is_admin(self):
        return False
