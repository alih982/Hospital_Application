# from django.contrib.auth.models import Group, User
from myapp.models import OTPRecord
from rest_framework import serializers

class OtpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OTPRecord
        fields = ['id', 'phone_number', 'otp', 'created_at', 'expires_at']

