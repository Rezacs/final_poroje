from django.db import models

from django.contrib.auth.models import AbstractUser
from custom_login.myusermanager import *


class MyUser ( AbstractUser ) :
    username = models.CharField(max_length=30 , blank=True , null=True)
    # user_name = models.CharField(max_length=30 , unique=True , blank=True , null=True)
    email = models.EmailField(('email address'), blank=True , null=True )
    mobile = models.CharField(max_length=11 , unique=True)
    otp = models.PositiveIntegerField(blank=True , null=True)
    otp_created_time = models.DateTimeField(auto_now=True)
    mobile_checked = models.BooleanField(null=True , blank=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'mobile'

    REQUIRED_FIELDS = []

    def __str__(self):
        #return str(self.mobile , self.username)
        return f'{self.username}'

    backend = 'custom_login.mybackend.ModelBackend'

    #objects = models.Manager()
