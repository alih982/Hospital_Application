from myapp.views import BaseView
from datetime import timedelta
import sys
from django.utils import timezone
# from myapp.Controllers.OTPController import otp_view
item_t = BaseView().model('item')

class ItemModel(BaseView):
    def get_items():
      result = item_t.objects.all()
     
    #   sys.exit(1)  
      return result

