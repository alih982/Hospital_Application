from django.shortcuts import render, redirect
from myapp.models import OTPRecord
import random
from django.shortcuts import render
import sys
from ..Models import ItemModel, OtpModel
from django.shortcuts import render
from ..models import OTPRecord
from ..Helpers import renderr
from rest_framework_simplejwt.tokens import RefreshToken

otp_t = OtpModel.OtpModel

class OtpService():
    @staticmethod
    def generate_otp():
      return str(random.randint(100000, 999999))
    
    def setCookieAndRedirect(name):
      redirect(name).set_cookie(
                key='access_token',
                value=str(redirect(name).access_token),
                httponly=True,
                secure=False,
                samesite='Lax',
                max_age=300
            )
      redirect(name).set_cookie(
                key='refresh_token',
                value=str(redirect(name)),
                httponly=True,
                secure=False,
                samesite='Lax',
                max_age=7 * 24 * 60 * 60
            )
    def refreshh(user):
      return RefreshToken.for_user(user)
       