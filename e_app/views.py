from django.shortcuts import render,HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.shortcuts import redirect
from .froms import *
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data.get('email')
            user.save()
            address = form.cleaned_data.get('address')
            user.profile.address = address
            user.profile.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    
    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context)


def index(request):
    # category = category
    products = Product.objects.all()
    context = {"products": products}
    return render(request , 'products/index.html',context=context)

@login_required
def add_product(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm

    context = {
        'form':form
    }
    
    return render(request,'products/add.html',context)

def update_product(request,pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('index')
    
    context = {
        'form': form
    }
    
    return render(request,'products/update.html',context)
      

def product_detail(request,pk):
    product = Product.objects.get(id = pk)
    context = {'product':product}
    return render(request,'products/detail.html',context)

@login_required(login_url='login')
def delete_product(request,pk):
    product = Product.objects.get(id = pk)
    product.delete()
    
    return redirect('index')

@login_required(login_url='login')
def customer_list(request):
    customer_list = Customer.objects.all()
    context = {
        'customers': customer_list
    }
    return render(request,'customer/index.html',context)

@login_required(login_url='login')
def add_customer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    context = {
        'form':form
    }
    
    return render(request,'customer/add.html',context)

@login_required(login_url='login')
def update_customer(request,pk):
    customer = Customer.objects.get(id = pk)
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST,instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    constext = {
        'form': form
    }
    
    return render(request,'customer/update.html',constext)
@login_required(login_url='login')
def delete_customer(request,pk):
    customer = Customer.objects.get(id = pk)
    customer.delete()
    return redirect('customer_list')

@login_required(login_url='login')
def order_list(request):
    orders = Order.objects.all()
    context = {
        'orders': orders,
    }
    return render(request,'order/index.html',context)

@login_required(login_url='login')
def add_order(request):
    form = OrderForm()
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('order_list')
    context = {
        'form': form
    }
    
    return render(request,'order/add.html',context)

@login_required(login_url='login')
def update_order(request,pk):
    order = Order.objects.get(id = pk)
    form = OrderForm(instance=order)
    
    if request.method == "POST":
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    context = {
        'form':form
    }
    return render(request,'order/update.html',context)

@login_required(login_url='login')
def delete_order(request,pk):
    order = Order.objects.get(id = pk)
    order.delete()
    return redirect('order_list')

