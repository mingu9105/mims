from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default="")
    # user_id = models.CharField(max_length=50, primary_key=True)
    # user_pw = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50, blank = True)
    user_name = models.CharField(max_length=50)
    user_num1 = models.CharField(max_length=50, blank = True)
    user_num2 = models.CharField(max_length=50, blank = True)
    user_years = models.CharField(max_length=50, blank = True)
    user_month = models.CharField(max_length=50, blank = True)
    user_day = models.CharField(max_length=50, blank = True)
    user_phone_1 = models.CharField(max_length=50, blank = True) 
    user_phone_2 = models.CharField(max_length=50, blank = True)
    user_address = models.CharField(max_length=50, blank = True)
    user_doctor_no = models.CharField(max_length=50, blank = True)
    user_hospital_no1 = models.CharField(max_length=50, blank = True)
    user_hospital_no2 = models.CharField(max_length=50, blank = True)
    user_hospital_no3 = models.CharField(max_length=50, blank = True)
    c_date = models.DateTimeField()