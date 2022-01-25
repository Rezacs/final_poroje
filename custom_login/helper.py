import datetime
from kavenegar import *
from custom_login.models import MyUser
from homew.settings import Kavenegar_API
from random import randint
from zeep import Client


def send_otp (mobile , otp) :
    mobile = [mobile , ]
    try:
        # api = KavenegarAPI( Kavenegar_API ) 
        # params = {
        #     'sender': '1000596446',#optional
        #     'receptor': mobile ,#multiple mobile number, split by comma
        #     'message': f'You OTP for Bi3z is : {otp}',
        # } 
        # response = api.sms_send(params)
        print('OTP :' , otp )
        # print(response)
    except APIException as e: 
        print(e)
    except HTTPException as e: 
        print(e)


def send_otp_soap (mobile , otp) :
    print('OTP :' , otp )
    client = Client('http://api.kavenegar.com/soap/v1.asmx?WSDL')
    receptor = [mobile ,]

    empty_array_placeholder = client.get_type('ns0:ArrayOfString')
    receptors = empty_array_placeholder()
    for item in receptor :
        receptors['string'].append(item)

    api_key = Kavenegar_API
    message = 'Your OTP is {}'.format(otp)
    sender= '1000596446'
    status = 0
    status_message = ''
    result = client.service.SendSimpleByApikey(
        api_key,
        sender,
        message,
        receptors,
        0,1,status,status_message,
    )
    print(result)


def get_random_otp() :
    return randint( 1000 , 9999)



def check_otp_expiration (mobile) :
    print('ssjjjjjjjjj')
    try :
        user = MyUser.objects.get(mobile = mobile )
        now = datetime.datetime.now()
        otp_time = user.otp_created_time
        dif_time = now - otp_time
        print('OTP Time  : ' , dif_time)
        if dif_time.seconds > 60 :
            return False
        return True
    except MyUser.DoesNotExist :
        return False