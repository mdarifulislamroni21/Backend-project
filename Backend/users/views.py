from django.shortcuts import render
from form.models import main_user,buyproduct
from form.form import main_users,buyproducts
# Create your views here.
def s_user(request):
    load_main_user=main_user.objects.order_by('user_name')

    diction={'main_user_data':load_main_user}
    return render(request,'pages/main_page/view_user.html',context=diction)
def view_user(request,user_id):
    load_main_user=main_user.objects.get(pk=user_id)
    load_buyproduct=buyproduct.objects.filter(user_name=user_id)
    diction={'main_user_data':load_main_user,'buyproduct_data':load_buyproduct}
    return render(request,'pages/argument/view_user.html',context=diction)
def edid_user(request,user_ids):
    load_main_user=main_user.objects.get(pk=user_ids)
    load_main_form=main_users(instance=load_main_user)
    diction={'edid_user_form':load_main_form}
    if request.method == 'POST':
        submit_data=main_users(request.POST,instance=load_main_user)
        if submit_data.is_valid():
            submit_data.save(commit=True)
            diction.update({'success':'Thank You! Your User Data Changed Successfully'})
    return render(request,'pages/argument/edid_user.html',context=diction)
#######

def edid_product(request,product_id):
    load_product=buyproduct.objects.get(pk=product_id)
    load_product_form=buyproducts(instance=load_product)
    diction={'edid_product':load_product_form}
    if request.method == 'POST':
        load_product_data=buyproducts(request.POST,instance=load_product)
        if load_product_data.is_valid():
            load_product_data.save(commit=True)
            diction.update({'success':'Thank You! Your Product Data Changed Successfully'})
    return render(request,'pages/argument/edid_product.html',context=diction)
