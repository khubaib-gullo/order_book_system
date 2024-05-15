from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import OrderForm
# Create your views here.
from .models import Container, Product, Order

def home(request):
    container = Container.objects.all()
    product = Product.objects.all()
    context = {
        "containers": container,
        "products": product,

    }
    return render(request, "base/home.html", context)



def order(request):
    form = OrderForm()
    context = {"form": form}
    if request.method == 'POST':

        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order')

    return render(request, "base/order.html", context)
