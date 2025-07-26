from django.views.generic import TemplateView
import sys
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from ..models import ChatMessage
from ..Helpers.helper import renderr
from django.shortcuts import render, redirect
import logging
from myapp.Models.UserModel import UserModel
import re
from django.http import HttpResponseBadRequest
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .forms.formServices import RegisterForm
from myapp.models import OTPRecord
from myapp.models import get_or_create_user
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

from myapp.Models.UserModel import UserModel
from myapp.AppLogic.OtpService import OtpService

from myapp.Models import MenuModel
from menuapp.views import ShowMenu
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
# from django.contrib.auth import authenticate, login
# from .forms import LoginForm
# Create your views here.

menuModel = MenuModel.MenuModel


otp_model = OTPRecord
otp_service = OtpService
clean_password_check = RegisterForm
user_Model = UserModel
menu = menuModel.showMenu()
# menuAddress = menuModel.showMenuAddress()
# sys.exit('ok')


class AuthenticateController():
    
    def getSignUpPage(request):
        return render(request, 'signup.html')
    def signUp(request):
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        message = ''
            # return render(request, 'signup.html', {
            #     'message': 'Phone is required',
            #     'show_otp_input': False,
            #     'phone': ''
            # })
        if phone_number:
            try:
                # checlking phone
                pattern = r'^09\d{9}$'  # فقط موبایل ایران با ۰۹ شروع و ۱۱ رقم
                if not re.match(pattern, phone_number):
                    
                    # return HttpResponseBadRequest("شماره موبایل نامعتبر است.")
                    message = "شماره موبایل نامعتبر است."
                else:
                    message = ""
                    if message == "":
                        otp = otp_service.generate_otp()
                        # sys.exit('ok')
                        
                        user_Model.addUser(phone_number, password, otp)
                        
                        response = render(request, 'login.html')
                        response.set_cookie('phone_number', phone_number)
                        return response
                
            except ValidationError as e:
                return render(request, 'signup.html', {'errors': message})

        #     if record.is_expired():
        #         return render(request, 'otp_page.html', {
        #             'message': '❌ OTP expired',
        #             'show_otp_input': True,
        #             'phone': phone
        #         })

        #     if record.otp != otp_input:
        #         return render(request, 'otp_page.html', {
        #             'message': '❌ Invalid OTP',
        #             'show_otp_input': True,
        #             'phone': phone
        #         })

        #     user, _ = get_or_create_user(phone)
        #     refresh = RefreshToken.for_user(user)


        #     response = redirect('panel')
        #     response.set_cookie(
        #         key='access_token',
        #         value=str(refresh.access_token),
        #         httponly=True,
        #         secure=False,
        #         samesite='Lax',
        #         max_age=300
        #     )
        #     response.set_cookie(
        #         key='refresh_token',
        #         value=str(refresh),
        #         httponly=True,
        #         secure=False,
        #         samesite='Lax',
        #         max_age=7 * 24 * 60 * 60
        #     )
        #     return response

        # otp = otp_service.generate_otp()
        # # expire_date = otp_tt.mintes_Expire5
        # otp_tt.update_OrCreate(phone, otp)
        # print(f"OTP for {phone}: {otp}")  # Replace with SMS service
        
        
        
        # sys.exit('ok')
        # user = user_Model.addUser(phone_number=phone_number, password=password)
        # user.set_password(password)
        # user.save()
        # users = UserModel.showUser()
        
        return render(request, 'login.html', {
            'message': message,
            'show_otp_input': True,
            'phone': phone_number
            # 'menu_zip': menu_zip
        })
        
    def verify_phone_number(request):
        return render(request, 'otp_page.html', {
            'show_otp_input': False,
            'message': '',
            'phone': ''
        })

    def post(request):
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
                record = otp_model.getRecord_Bynumber(phone)
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

        otp = otp_model.generate_otp()
        # expire_date = otp_tt.mintes_Expire5
        otp_model.update_OrCreate(phone, otp)
        print(f"OTP for {phone}: {otp}")  # Replace with SMS service

        return render(request, 'signup.html', {
            'message': f'✅ OTP is {otp}',
            'show_otp_input': True,
            'phone': phone
        })
    def home_page(request):
        return render(request, 'index-three.html')
    def login(request):
        if request.method == 'POST':
            phone = request.POST.get('phone_number')
            password = request.POST.get('password')
            message = ""

            user_pass = user_Model.otp_by_phone_number(phone)

            if not user_pass or password != user_pass.password:
                message = 'رمز نا معتبر است'
                return render(request, 'login.html', {'message': message})

            # ✅ Mark user as authenticated
            
            user_pass.is_authenticated = 1
            user_pass.save()

            response = redirect('home')
            response.set_cookie('phone_number', phone)
            return response

        return render(request, 'login.html')

    
    def postLogin(request):
        phone = request.POST.get('phone_number')
        password = request.POST.get('password')
        
        user_pass = user_Model.otp_by_phone_number(phone)

        if not user_pass or password != user_pass.password:
            message = 'رمز نا معتبر است'
            return render(request, 'login.html', {'message': message})
        user_phone = user_Model.get_user(phone)
        user_is_auth =user_phone.is_authenticated
        if user is not None and user_is_auth:
            user = authenticate(request, username=phone, password=password)
            
            login(request, user)
            response = render(request, 'index-three.html', {
                'user_pass': user_pass,
                'phone': phone
            })
            response.set_cookie('phone_number', phone)
            
            return response

        # return render(request, 'login.html')
