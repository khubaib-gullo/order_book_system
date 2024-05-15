from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Container(models.Model):
    container_name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    receive_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.container_name



class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    container_id = models.ForeignKey(Container, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name



class Order(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    address = models.TextField(null=False, blank=False)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    order_update_date = models.DateTimeField(auto_now=True)
    phone_no = models.CharField(max_length=12)
    delivery_fee = models.FloatField(default=150)
    total_items = models.IntegerField(null=True)



    #
    def __str__(self):
        return self.phone_no





