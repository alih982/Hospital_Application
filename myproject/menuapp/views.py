from django.shortcuts import render
from myapp.Models import MenuModel
from django.views.generic.base import ContextMixin
from .models import Menu
from django.http import HttpResponse
# Create your views here.
import sys
menuModel = MenuModel.MenuModel
class ShowMenu(ContextMixin):
    def showMenuu(request):
        menu = menuModel.showMenu()
        phone_n = request.COOKIES.get('phone_number')
        message = ""
        menu_auth = menuModel.show_menu_for_authenticated_users()
        print(phone_n)
        is_auth_user = menuModel.show_ifauthenticated_user(phone_n)
        # if is_auth_user == True:
        return render(request, 'index-three.html', {
            'menu': menu,
            'menu_auth': menu_auth,
            'user_pass': is_auth_user,
            'user_is_auth': is_auth_user

        })
            
        # else:
        #     return render(request, 'index-three.html', {
        #     'menu': menu,
        #     'menu_auth': menu_auth,
        #     'user_pass': is_auth_user,
        #     'user_is_auth': is_auth_user
        # })

    # def get_context_data(self, *args,**kwargs):
    #         context = super().get_context_data(*args, **kwargs)
    #         context = Menu.objects.all()
    #         return context