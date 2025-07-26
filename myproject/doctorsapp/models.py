from django.db import models

# Create your models here.
class Doctors(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    user_type_id = models.IntegerField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    otp = models.IntegerField()
    is_active = models.IntegerField()
    city = models.CharField(max_length=255)
    city_id = models.IntegerField()
    province = models.CharField(max_length=255)
    province_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'doctors'

class Province(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    tel_prefix = models.CharField(max_length=10)

    class Meta:
        db_table = 'provinces'
        managed = False  # چون داده‌ها از بیرون وارد شدن، Django نباید مدیریت ایجاد/حذف جدول رو انجام بده

    def __str__(self):
        return self.name