from django.contrib import admin

# Register your models here.

from .models import Container, Product, Order


admin.site.register(Container)
admin.site.register(Product)
admin.site.register(Order)


