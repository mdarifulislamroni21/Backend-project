from django import forms
from form.models import main_user,buyproduct
class main_users(forms.ModelForm):
    # user_name=forms.CharField(widget={forms.TextInput(attrs={'placeholder':'Enter Your User Name'})})
    # password=forms.CharField(widget={forms.TextInput(attrs={'placeholder':'Enter Your Password','type':'password'})})
    # email=forms.CharField(widget={forms.TextInput(attrs={'placeholder':'Enter Your Email'})})
    # phone_no=forms.CharField(widget={forms.TextInput(attrs={'placeholder':'Enter Your Phone Namber'})})
    class Meta:
        model=main_user
        fields="__all__"
class buyproducts(forms.ModelForm):
    class Meta:
        model=buyproduct
        fields="__all__"
