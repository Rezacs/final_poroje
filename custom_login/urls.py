from django.urls import path
from custom_login.views import *

urlpatterns = [
    path('register' , register , name='otp-register' ) ,
    path('login' , mobile_login , name='mobile_login' ) ,
    path('dashboard' , dashboard , name='mobile-dashboard' ) ,
    path('verify' , verify , name='verify' ) ,
]
