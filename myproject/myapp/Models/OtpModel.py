from myapp.views import BaseView
from django.utils import timezone
from datetime import timedelta

from myapp.models import OTPRecord
import random

otp_t = OTPRecord

# otp_t = BaseView().model('otp')


class OtpModel(BaseView):

    def get_otpbyNumber(phone):
        result = otp_t.objects.filter(phone_number=phone).latest('created_at')
        return result


    def createOtp(phone, otp):
        result = otp_t.objects.create(
            phone_number=phone,
            otp=otp,
            expires_at=timezone.now() + timedelta(minutes=5)
        )
        return result
    
    def get_recordByphone(phone):
        result = otp_t.objects.filter(phone_number = phone).latest('expires_at')
        return result
    @staticmethod
    def getRecord_Bynumber(phone):
        result = OTPRecord.objects.filter(phone_number=phone).order_by('expires_at').last()
        return result
    def mintes_Expire5():
        return timezone.now() + timedelta(minutes=5)
    @staticmethod
    def update_OrCreate(phone, otp):
        fiveminutes = timezone.now() + timedelta(minutes=5)
        result = OTPRecord.objects.update_or_create(
            phone_number=phone,
            defaults={
                'otp': otp,
                'expires_at': fiveminutes
            }
        )
        return result
    @staticmethod
    def generate_otp():
        res = random.randint(9999, 100000)
        return res
    
    def save(self, *args, **kwargs):
        # Set expiration to 5 minutes from creation
        if not self.expires_at:
            self.expires_at = timezone.now() + timedelta(minutes=5)
        super().save(*args, **kwargs)
        
    def is_expired(self):
        return timezone.now() > self.expires_at
        