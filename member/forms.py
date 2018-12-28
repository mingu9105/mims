from django import forms

from django.contrib.auth.forms import UserCreationForm

from member.models import Member
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = (
            'user_name',
            'user_num1',
            'user_num2',
            'user_years',
            'user_month',
            'user_day',
            'user_phone_1',
            'user_phone_2',
            'user_address',
            'user_doctor_no',
            'user_hospital_no1',
            'user_hospital_no2',
            'user_hospital_no3',
            'c_date',)
