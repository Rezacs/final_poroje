from django.urls import path
from custom_login.views import *

urlpatterns = [
    path('register' , register , name='register' ) ,
    path('mobile_login' , mobile_login , name='mobile_login' ) ,
    path('dashboard' , dashboard , name='dashboard' ) ,
    path('verify' , verify , name='verify' ) ,
]
