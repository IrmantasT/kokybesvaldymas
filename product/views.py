from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ProductForm
from .models import Product


def post_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('.')
    else:
        form = ProductForm()
        all_prod = Product.objects.all
    return render(request, 'production.html', {'form':form,'all':all_prod})


def all_production(request):
    all_prod = Product.objects.all
    return render(request, 'getproduct.html',{'all':all_prod})