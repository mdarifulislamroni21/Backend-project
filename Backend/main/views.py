from django.shortcuts import render
from form.form import main_users,buyproducts
from django.contrib.auth.models import User
from login.models import UserInfo
# Create your views here.
#for http://127.0.0.1:8000
def home(request):
    return render (request,'pages/main_page/home.html')

#for http://127.0.0.1:8000/registration/
def registration(request):
    main_user_data=main_users()
    dictrion={'main_user_form':main_user_data}
    if request.method == 'POST':
        main_user_data=main_users(request.POST)
        if main_user_data.is_valid():
            main_user_data.save(commit=True)
            dictrion.update({'submit_success':"Registration Form Submit Successfully"})

    return render(request,'pages/main_page/Registration.html',context=dictrion)
def buyproduct(request):
    buyproduct_data=buyproducts()
    dictionpas={'buyproduct_form':buyproduct_data}
    if request.method == 'POST':
        buyproduct_data=buyproducts(request.POST)
        if buyproduct_data.is_valid():
            buyproduct_data.save(commit=True)
            dictionpas.update({'submit_success':"Prodact Added Successfully"})
    return render (request,'pages/main_page/buyproduct.html',context=dictionpas)
def profile_details(request):
    diction={}
    if  request.user.is_authenticated:
        load_data=request.user
        user_id=load_data.id
        defult_user=User.objects.get(pk=user_id)
        make_user=UserInfo.objects.get(user__pk=user_id)
        diction={'defult_users':defult_user,'make_user_pass':make_user}


    return render (request,'pages/main_page/profile.html',context=diction)
