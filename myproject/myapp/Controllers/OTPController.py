from django.shortcuts import render, redirect
from django.views import View
from django.utils import timezone

from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.conf import settings

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

from myapp.models import OTPRecord
from myapp.AppLogic.OtpService import OtpService
from myapp.models import OTPRecord, User
from myapp.Models import OtpModel
from myapp.models import User 
from myapp.AppLogic.OtpService import OtpService
from myapp.models import get_or_create_user
from myapp.Models import MenuModel

menuModel = MenuModel.MenuModel
otp_service = OtpService()
otp_tt = OtpModel.OtpModel()
otp_service = OtpService()
user_tt = User()

class OTPController(View):
    def get(self, request):
        return render(request, 'otp_page.html', {
            'show_otp_input': False,
            'message': '',
            'phone': ''
        })

    def post(self, request):
        phone = request.POST.get('phone')
        otp_input = request.POST.get('otp')

        if not phone:
            return render(request, 'otp_page.html', {
                'message': 'Phone is required',
                'show_otp_input': False,
                'phone': ''
            })

        if otp_input:
            try:
                record = otp_tt.getRecord_Bynumber(phone)
            except OTPRecord.DoesNotExist:
                return render(request, 'otp_page.html', {
                    'message': '❌ No OTP found',
                    'show_otp_input': True,
                    'phone': phone
                })

            if record.is_expired():
                return render(request, 'otp_page.html', {
                    'message': '❌ OTP expired',
                    'show_otp_input': True,
                    'phone': phone
                })

            if record.otp != otp_input:
                return render(request, 'otp_page.html', {
                    'message': '❌ Invalid OTP',
                    'show_otp_input': True,
                    'phone': phone
                })

            user, _ = get_or_create_user(phone)
            refresh = RefreshToken.for_user(user)


            response = redirect('panel')
            response.set_cookie(
                key='access_token',
                value=str(refresh.access_token),
                httponly=True,
                secure=False,
                samesite='Lax',
                max_age=300
            )
            response.set_cookie(
                key='refresh_token',
                value=str(refresh),
                httponly=True,
                secure=False,
                samesite='Lax',
                max_age=7 * 24 * 60 * 60
            )
            return response

        otp = otp_service.generate_otp()
        # expire_date = otp_tt.mintes_Expire5
        otp_tt.update_OrCreate(phone, otp)
        print(f"OTP for {phone}: {otp}")  # Replace with SMS service

        return render(request, 'otp_page.html', {
            'message': f'✅ OTP is {otp}',
            'show_otp_input': True,
            'phone': phone
        })


def panel_view(request):
    access_token = request.COOKIES.get('access_token')
    if not access_token:
        return redirect('otp_page')

    jwt_auth = JWTAuthentication()
    try:
        validated_token = jwt_auth.get_validated_token(access_token)
        print(validated_token)
        user = jwt_auth.get_user(validated_token)
    except Exception as e:
      print(f"User fetch error: {e}")
      return redirect('otp_page')

    return render(request, 'panel.html', {'user': user})



def log_out(request):
    # menu = menuModel.showMenu()
    # menuAddress = menuModel.showMenuAddress()
    # menu_zip = zip(menu, menuAddress)    
    return render(request, 'index-three.html'
                #   ,
                #   {'menu_zip':menu_zip}
                  )
    
    
    

    
    

from django.db import models



