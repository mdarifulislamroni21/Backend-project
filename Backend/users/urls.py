from django.conf.urls import url
from django.urls import path
from users import views

urlpatterns=[
path('',views.s_user,name="s_user"),
path('view_user/<int:user_id>/',views.view_user,name="view_user"),
path('edid_user/<int:user_ids>/',views.edid_user,name="edid_user"),
path('edid_product/<int:product_id>/',views.edid_product,name="edid_product"),

]
