from django.urls import path
from custom_login.views import *

urlpatterns = [
    path('mobile_login' , mobile_login , name='mobile_login' ) ,
    path('dashboard' , dashboard , name='dashboard' ) ,
]
