from kavenegar import *
from homew.settings import Kavenegar_API
from random import randint


def send_otp (mobile , otp) :
    mobile = [mobile , ]
    try:
        api = KavenegarAPI( Kavenegar_API , timeout=20 ) 
        params = {
            'sender': '',#optional
            'receptor': mobile ,#multiple mobile number, split by comma
            'message': f'You OTP is : {otp}',
        } 
        response = api.sms_send(params)
        print(response)
    except APIException as e: 
        print(e)
    except HTTPException as e: 
        print(e)
        
    print('OTP :' , otp )

def get_random_otp() :
    return randint( 1000 , 9999)