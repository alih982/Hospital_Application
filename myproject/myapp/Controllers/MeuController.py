import sys
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from ..models import ChatMessage
from ..Helpers.helper import renderr
from django.shortcuts import render, redirect
import logging


class MenuController():
    
    def pharmacy(request):
        return render(request, 'pharmacy-shop.html')
    def aboutUs(request):
        return render(request, 'aboutus.html')
    def contactUs(request):
        return render(request, 'contact.html')
    def doctors_team(request):
        return render(request, 'doctor-team-three.html')