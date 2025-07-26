# from django.shortcuts import render
# from myapp.models import Item
# import sys
# from pprint import pprint
# def showStudents(request):
#     # Get all items from the database
#     items = Item.objects.all()
    
#     # Prepare a list of dictionaries with the relevant data
#     item_data = [{'name': item.name, 'age': item.age, 'email': item.email} for item in items]
#     print(item_data)
#     context = {
#         'item_data': item_data,  # Pass the structured list to the template
#     }
    
#     # Pass items to the template
#     return render(request, 'home.html', context)
from django.views import View
from myapp.models import Item, OTPRecord


class BaseView(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.models = {
            'item': Item,
            'otp': OTPRecord
        }
    def model(self, name):
        return self.models.get(name)
