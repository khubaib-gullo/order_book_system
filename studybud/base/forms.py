from django.forms import ModelForm
from .models import Container, Product, Order


class ContainerForm(ModelForm):
    class Meta:
        model = Container
        fields = "__all__"


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
