from django.contrib import admin
from django.urls import path, include
from myapp import views
from .Controllers import ItemController, OTPController
from .views import showStudents
from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from myapp.Controllers.NewController import JwtPhoneView

# router = DefaultRouter()
# router.register(r'users', JwtPhoneView)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', ItemController.show_items, name='show_students'),
    # path('otp/', OTPController.otp_view, name='otp'),
    path('', include('myapp.urls')),
    
]

