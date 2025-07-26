# myapp/models.py
from django.db import models
import sys
# from django.contrib.auth.hashers import make_password, check_password
from django.db import models
from django.utils import timezone
from datetime import timedelta

class User(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    phone_number = models.CharField(max_length=11, unique=True)  # مثل 09123456789
    password = models.CharField(max_length=255, null=True, blank=True)
    otp = models.IntegerField(null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    is_authenticated = models.IntegerField(default=0)
    # def set_password(self, raw_password):
    #     self.password = make_password(raw_password)

    # def check_password(self, raw_password):
    #     return check_password(raw_password, self.password)

    # def __str__(self):
    #     return self.phone_number
from django.db import models

# Create your models here.
class Menu(models.Model):
    
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=500, null=True, blank=True)  # یا URLField اگر فقط لینک وب هست
    is_authenticated = models.IntegerField(default=0)
    

    class Meta:
        db_table = 'menu'
def menu_context(request):
    phone = request.COOKIES.get('phone_number')
    user = None
    is_auth_user = False
    user_phone_number = ''
    message = ''

    if phone:
        try:
            user = User.objects.get(phone_number=phone)
            if user.is_authenticated:
                message = "1 bod"
            else:
                message = "0 bod"
            is_auth_user = user.is_authenticated
            user_phone_number = user.phone_number
            message = "User found"
        except User.DoesNotExist:
            message = "User not found"

    menu_auth = Menu.objects.filter(is_authenticated=True)
    menu = Menu.objects.filter(is_authenticated=False)

    return {
        'menu_auth': menu_auth,
        'menu': menu,
        'user': phone,
        'user_pass': user,
        'user_phone': user_phone_number,
        'user_is_auth': is_auth_user,
        'unauth_user': not is_auth_user,
        'message': message
    }




def dashboard(request):
    phone = request.COOKIES.get('phone_number')
    return {
        'user_pass': phone
    }