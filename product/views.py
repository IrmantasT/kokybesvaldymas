from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import ProductForm
from .models import Product


@login_required(login_url='/login/')
def post_product(request):
    context = {}
    if request.method == 'POST':
        form = ProductForm(request.POST)
        # form.user = request.user
        if form.is_valid():
            form.user = request.user.id
            form.save()
            return HttpResponseRedirect('.')
    else:
        user = request.user
        form = ProductForm(initial={'user':user})
        all_prod = Product.objects.all
        context = {'form':form,'all':all_prod}
    return render(request, 'production.html', context)


def all_production(request):
    all_prod = Product.objects.all
    return render(request, 'getproduct.html',{'all':all_prod})



def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'production.html', {'form': form, 'all': all_prod})
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...