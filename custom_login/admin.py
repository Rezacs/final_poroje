from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class UserAdmin(admin.ModelAdmin) :
    list_display = ('mobile' , 'username' , 'pk' )
    # list_filter = ('title', 'shortdesc' , 'status' , 'created_on' , 'category')

admin.site.register(MyUser , UserAdmin)


# Register your models here.
