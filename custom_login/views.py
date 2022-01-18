from logging import raiseExceptions
from django.shortcuts import render
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from custom_login.models import *
from custom_login.forms import *
from custom_login.helper import *

def mobile_login ( request ) :
    if request.method == "POST" :
        if "mobile" in request.POST :
            mobile = request.POST.get('mobile')
            try :
                user = MyUser.objects.get(mobile=mobile)
                login(request , user)
            except :
                raiseExceptions
            return HttpResponseRedirect(reverse('mobile-dashboard'))
    return render ( request , 'mobile_login.html')

def dashboard ( request ) :
    return render ( request , 'dashboard.html')

def register ( request ) :
    form = RegisterForm
    if request.method == 'POST' :
        try :
            if 'mobile' in request.POST :
                mobile = request.POST.get('mobile')
                user = MyUser.objects.get(mobile=mobile)
                otp = get_random_otp()
                send_otp(mobile , otp)
                user.otp = otp
                user.save()
                return HttpResponseRedirect(reverse('verify'))

        except MyUser.DoesNotExist :
            form = RegisterForm(request.POST)
            if form.is_valid () :
                user = form.save(commit=False)
                # send OTP
                otp = get_random_otp()
                send_otp(mobile , otp)
                user.otp = otp
                user.save()
                user.is_active = False
                user.save()
                return HttpResponseRedirect(reverse('verify'))
                
    return render ( request , 'verify.html' , {'form' : form })

def verify ( request ) :
    return render (request , 'verify.html' )
