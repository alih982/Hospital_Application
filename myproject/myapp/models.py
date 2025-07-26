# myapp/models.py
from django.db import models
import sys
# from django.contrib.auth.hashers import make_password, check_password
from django.db import models
from django.utils import timezone
from datetime import timedelta
from menuapp.models import User
class Item(models.Model):  # Should be SINGULAR: Item, not Items
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    db_table = 'item'
    
    


    


class OTPRecord(models.Model):
    phone_number = models.CharField(max_length=15)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    db_table = 'otprecord'



    

    

class ChatMessage(models.Model):
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    db_table = 'chatmessage'
    

    
    # @staticmethod

def get_or_create_user(phone):
    return User.objects.get_or_create(username=phone)

    
from django.db import models
# from django.contrib.auth.models import User
from django.utils import timezone

class UserToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    db_table = 'usertoken'

    


