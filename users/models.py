from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
  username = None
  email = models.EmailField(_('Email address'), unique=True)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  objects = CustomUserManager()

  def __str__(self):
    return self.email
