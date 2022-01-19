from logging import raiseExceptions
from django.shortcuts import render
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from custom_login.models import *
from custom_login.forms import *
from custom_login.helper import *
from django.contrib import messages


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
                # send_otp_soap(mobile , otp)
                user.otp = otp
                user.otp_created_time = datetime.datetime.now()
                user.save()
                request.session['user_mobile'] = user.mobile
                return HttpResponseRedirect(reverse('verify'))

        except MyUser.DoesNotExist :
            form = RegisterForm(request.POST)
            if form.is_valid () :
                user = form.save(commit=False)
                # send OTP
                otp = get_random_otp()
                send_otp(mobile , otp)
                # send_otp_soap(mobile , otp)
                user.otp = otp
                user.otp_created_time = datetime.datetime.now()
                user.save()
                user.is_active = False
                user.save()
                request.session['user_mobile'] = user.mobile
                return HttpResponseRedirect(reverse('verify'))
                
    return render ( request , 'register.html' , {'form' : form })

def verify ( request ) :
    try :
        mobile = request.session.get('user_mobile')
        user = MyUser.objects.get(mobile = mobile)
        if request.method == 'POST' :
            print('sssssssss0')
            # check otp expiration 
            if not check_otp_expiration(user.mobile) :
                print('ssssssssssssssss')
                return HttpResponseRedirect(reverse('register'))
            if user.otp != int(request.POST.get('otp')) :
                print('sssssssssss1')
                return HttpResponseRedirect(reverse('register'))
            
            print('sssssssssss2')
            user.is_active = True
            user.save()
            login(request , user)
            messages.add_message(request, messages.SUCCESS, 'Logged In successfully')
            return redirect(reverse('dashboard'))
        return render (request , 'verify.html' , {'mobile' : mobile })
    except :
        return HttpResponseRedirect(reverse('register'))
