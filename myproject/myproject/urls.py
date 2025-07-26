"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from myapp import views
from myapp.Controllers import ItemController, OTPController, NewController
from myapp.Controllers import ChatController
from rest_framework.authtoken import views

from django.urls import path
from django.contrib import admin
from myapp.Controllers import OTPController, ItemController, ChatController, NewController, AuthenticateController
from myapp.Controllers.MeuController import MenuController
from menuapp.views import ShowMenu
# from myapp.Controllers import AuthenticateController



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ShowMenu.showMenuu, name='home'),
    # path('', OTPController.log_out, name='home'),
    path('signUp/', AuthenticateController.AuthenticateController.getSignUpPage, name='sign_up_start'),
    path('verification/', AuthenticateController.AuthenticateController.signUp, name='sign_up'),
    path('signIn/', AuthenticateController.AuthenticateController.login, name='login_start'),
    # path('signInVerify/', AuthenticateController.AuthenticateController.postLogin, name='login'),
    path('pharmacy/', MenuController.pharmacy, name='pharmacy'),
    path('aboutUs/', MenuController.aboutUs, name='aboutUs'),
    path('contactUs/', MenuController.contactUs, name='contactUs'),
    path('doctors-team/', MenuController.doctors_team, name='doctors_team'),
    # path('otp/', OTPController.OTPController.as_view(), name='otp'),               # API endpoint for sending/checking OTP
    path('otp/', OTPController.OTPController.as_view(),  name='otp_page'),      # HTML page view
    path('panel/', OTPController.panel_view, name='panel'),

    # Chat
    path('chat/', ChatController.chat_page, name='chat'),
    path('chat/send/', ChatController.send_message, name='chat_send'),
    # path('panel/', OTPController.OTPController.go_p, name='panel'),

    # API
    path('api/', NewController.JwtPhoneView.as_view(), name='encrypted_phones'),
    # path('logout/', AuthenticateController.log_out),
]
