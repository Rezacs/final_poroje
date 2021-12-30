from django import forms
from custom_login.models import *

class RegisterForm ( forms.ModelForm ) :
    class Meta:
        model = MyUser
        fields = ['mobile']