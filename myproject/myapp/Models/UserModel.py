from django.db import models
from menuapp.models import User
from myapp.views import BaseView
import sys
class UserModel(BaseView):
    @staticmethod
    def addUser(username, password, otp, email=None):
        user = User.objects.create(
        phone_number=username,
        otp = otp,
        password=password or "",
        is_authenticated = 1
        )
        return user
    def showUser():
        rse = User.objects.all()
        return rse
    def otp_by_phone_number(phone):
        user_otp = User.objects.get(phone_number = phone, is_authenticated=1)
        return user_otp
    def get_user(phone):
        get_user = User.objects.get(phone_number=phone)
        return get_user
#     @staticmethod
#     def get_or_create_user(phone):
#         return User.objects.get_or_create(username=phone)