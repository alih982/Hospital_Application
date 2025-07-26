from django.utils import timezone
from datetime import timedelta
from django.db import models
from menuapp.models import Menu
from myapp.views import BaseView
from menuapp.models import User
import sys
class MenuModel(BaseView):
    def showMenu():
        res = Menu.objects.filter(is_authenticated = 0)
        return res
    def show_menu_for_authenticated_users():
        res = Menu.objects.filter(is_authenticated=1)
        return res
    def show_ifauthenticated_user(phone):
        res = User.objects.filter(is_authenticated=1, phone_number =phone).exists()
        return res
    def menu_auth():
        res = Menu.objects.filter(is_authenticated=1)
        return res
    # def showMenuAddress():
        
        # l = Menu.objects.all()
        # return l
# def dynamic_menu(request):
    
#     user_type = None
#     if request.user.is_authenticated:
#         if hasattr(request.user, 'user_type'):
#             user_type = request.user.user_type
#         elif request.user.is_superuser:
#             user_type = 'admin'
#         else:
#             user_type = 'user'
    
#     menus = Menu.objects.filter(user_type=user_type) if user_type else []
#     return {'menu_items': menus}