from django.db import models
from django.urls import reverse
# Create your models here.
country=(
('','-------Select Country-------'),
('Bangladesh','Bangladesh'),
('India','India'),('Pakistan','Pakistan'),
('NewYork','New York')
)


class main_user(models.Model):
    user_name=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    email=models.EmailField()
    phone_no=models.CharField(max_length=30)
    country=models.CharField(max_length=30,choices=country)
    def __str__(self):
        return self.user_name
    def get_absolute_url(self):
        return reverse('s_user')


class buyproduct(models.Model):
    user_name=models.ForeignKey(main_user,on_delete=models.CASCADE,related_name='products')
    product=models.CharField(max_length=25)
    price=models.IntegerField()
    def get_absolute_url(self):
        return reverse('edid_product',kwargs={'product_id':self.pk})
