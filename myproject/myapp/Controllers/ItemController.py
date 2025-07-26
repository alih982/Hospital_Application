from django.shortcuts import render
import sys
from ..Models import ItemModel
from django.shortcuts import render

model = ItemModel.ItemModel

def show_items(request):
    all_items = model.get_items
    return render(request, 'home.html', {
        'items': all_items
    })