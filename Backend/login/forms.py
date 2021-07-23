from django import forms
from login.models import UserInfo
from django.contrib.auth.models import User
class defult_user(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','password','email')
#UserInfo class
class user_info_form(forms.ModelForm):
    class Meta:
        model=UserInfo
        fields=('phone_no','facebook_id','profile_pic')
