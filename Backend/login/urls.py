from django.conf.urls import url
from django.urls import path
from login import views
urlpatterns=[
   path('',views.flogin,name='flogin'),
   path('login/',views.user_login,name='user_login'),
   path('login_check/',views.login_check,name="login_check"),
   path('logout/',views.user_logout,name="user_logout")
]
