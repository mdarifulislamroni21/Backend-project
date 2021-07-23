from django.shortcuts import render
from login.forms import defult_user,user_info_form
from login.models import UserInfo
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.
def flogin(request):
    diction={}
    load_defult_form=defult_user()
    load_user_info=user_info_form()
    diction={'defult_user':load_defult_form,'user_info':load_user_info}
    if request.method == 'POST':
        load_defult_form=defult_user(data=request.POST)
        load_user_info=user_info_form(data=request.POST)
        if load_defult_form.is_valid() and load_user_info.is_valid():
            user=load_defult_form.save()
            user.set_password(user.password)
            user.save()
            load_user_load=load_user_info.save(commit=False)
            load_user_load.user=user
            if 'profile_pic' in request.FILES:
                load_user_load.profile_pic=request.FILES['profile_pic']
            load_user_load.save()
            diction.update({'success':'Congragulate!! You are Registration Successfull'})
    else:
        load_defult_form=defult_user()
        load_user_info=user_info_form()

    return render (request,'pages/main_page/flogin.html',context=diction)
def user_login(request):

    return render (request,'pages/main_page/login.html')
def login_check(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("You Are Not Actived")

        else:
            return HttpResponse("Invalid Username Or Password")
    else:
        HttpResponseRedirect(reverse('user_login'))
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))
