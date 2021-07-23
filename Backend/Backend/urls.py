from django.contrib import admin
from django.urls import path
from main import views
from django.conf.urls import include
from django.conf import settings
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns

app_name='Backend'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('registration/',views.registration,name='registration'),
    path('buyproduct/',views.buyproduct,name="buyproduct"),
    path('users/',include('users.urls'),name="user"),
    path('flogin/',include('login.urls')),
    path('profile/',views.profile_details,name='profile'),
    path('classbase/',include('classbase.urls')),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
