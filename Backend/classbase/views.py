from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from login import models
from form.models import main_user,buyproduct
from django.urls import reverse_lazy
# Create your views here.
class homeclass(View):
    def get(self,request):
        return HttpResponse ("Hello This Is Working")
class template_view(TemplateView):
    template_name='indexs.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['frist']="Hello Frist Is Working"
        return context
class list_view(ListView):
    context_object_name='UsersInfo'
    model=models.UserInfo
    template_name='classbase/listview.html'
class details_view(DetailView):
    context_object_name='detail_views'
    model=models.UserInfo
    template_name='classbase/detailview.html'
class user_list_view(ListView):
    context_object_name='user_list'
    model=main_user
    template_name='classbase/user_list_view.html'
class user_details(DetailView):
    context_object_name='user_details'
    model=main_user
    template_name='classbase/user_detail_view.html'
class userproduct(DetailView):
    context_object_name='user_product'
    model=main_user
    template_name='classbase/user_product.html'
class add_product(CreateView):
    model=buyproduct
    fields="__all__"
    template_name='classbase/add_product_form.html'
class update_user(UpdateView):
    model=main_user
    fields=('user_name','phone_no','country')
    template_name='classbase/update_user.html'
class delete_product(DeleteView):
    model=buyproduct
    success_url=reverse_lazy('home')
    template_name='classbase/delete_product.html'
