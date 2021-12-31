from django.db import models

from django.contrib.auth.models import AbstractUser
from custom_login.myusermanager import *


class MyUser ( AbstractUser ) :
    username = None
    mobile = models.CharField(max_length=11 , unique=True)
    otp = models.PositiveIntegerField(blank=True , null=True)
    otp_created_time = models.DateTimeField(auto_now=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'mobile'

    REQUIRED_FIELDS = []

    backend = 'custom_login.mybackend.ModelBackend'

    #objects = models.Manager()
