from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from .forms import ProductForm, SearchForm
from .models import Product, User



@login_required(login_url='/login/')
def post_product(request):
    context = {}
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = User.objects.get(id=request.user.id)
            product.save()
            return HttpResponseRedirect('.')
    else:
        form = ProductForm()
        all_prod = Product.objects.all
        context = {'form':form,'all':all_prod}
    return render(request, 'production.html', context)


def all_production(request):
    all_prod = Product.objects.all
    return render(request, 'getproduct.html',{'all':all_prod})


def getrepare(request):
   if request.method == 'GET':
       form = SearchForm(request.GET)
       search = request.GET.get('search')
       post = Product.objects.all().filter(serial_no=search)
       return render(request, 'repare.html', {'post':post, 'form':form})