from django.contrib.auth.backends import ModelBackend
from custom_login.models import *
from custom_login.helper import *

class MobileBackend (ModelBackend ) :
    def authenticate(self, request, username=None , password=None , **kwargs ):
        mobile = kwargs['mobile']
        try :
            user = MyUser.objects.get(mobile = mobile )
        except MyUser.DoesNotExist :
            pass

class OtpBackend(ModelBackend) :
    def authenticate(self , request , email=None , password=None , **kwargs) :
        try :
            user = MyUser.objects.get(mobile = kwargs['mobile'] )
            otp = user.otp
            if str(otp) == str(password) :
                if check_otp_expiration(user.mobile) :
                    return user
            else :
                return None
        except Exception :
            return None
