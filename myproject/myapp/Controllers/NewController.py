import jwt
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from myapp.models import OTPRecord
import json
from myproject.serializers import OtpSerializer

class JwtPhoneView(APIView):
    def get(self, request):
        records = OTPRecord.objects.all()
        serializer = OtpSerializer(records, many=True)
        data = serializer.data
        
        secret = settings.SECRET_KEY
        
        for item in data:
            phone = item['phone_number']
            token = jwt.encode({'phone': phone}, secret, algorithm='HS256')
            item['phone_jwt'] = token
            # می‌تونی شماره اصلی رو حذف کنی:
            # del item['phone_number']
        
        return Response(data)
