from django.conf.urls import url
from django.urls import path
from classbase import views
urlpatterns=[
   path('',views.homeclass.as_view(),name="classbase"),
   path('template/',views.template_view.as_view(),name='template'),
   path('listview/',views.list_view.as_view(),name="list_view"),
   path('detail_view/<pk>/',views.details_view.as_view(),name='details_view'),
   path('user_list/',views.user_list_view.as_view(),name="user_list"),
   path('user_detail/<pk>/',views.user_details.as_view(),name='user_details'),
   path('user_product/<pk>/',views.userproduct.as_view(),name='user_products'),
   path('addproduct/',views.add_product.as_view(),name="add_product"),
   path('update_user/<pk>/',views.update_user.as_view(),name='update_user'),
   path('delete_product/<pk>/',views.delete_product.as_view(),name='delete_product')
]
