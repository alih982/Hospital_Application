from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from datetime import timedelta

class User(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    phone_number = models.CharField(max_length=11, unique=True)  # مثل 09123456789
    password = models.CharField(max_length=255, null=True, blank=True)
    is_staff = models.BooleanField(default=False, null=True)
    is_active = models.BooleanField(default=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    is_authenticated = models.BooleanField(default=False)