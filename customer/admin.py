from django.contrib import admin

from .models import *

class CustomerAdmin(admin.ModelAdmin) :
    list_display = ('mobile' ,'pk')

admin.site.register(Customer , CustomerAdmin)
admin.site.register(Payment)
admin.site.register(Address)

# Register your models here.
