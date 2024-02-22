from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from .froms import *
from .models import *

# User registration view
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # Load the profile instance created by the signal
            user.profile.email = form.cleaned_data.get('email')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()

    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context)



# Homepage view
def index(request):
    try:
        products = Product.objects.all()
    except Product.DoesNotExist:
        products = []
    context = {"products": products}
    return render(request, 'home.html', context=context)


# product list view
def product_list(request):
    try:
        products = Product.objects.all()
    except Product.DoesNotExist:
        products = []
    context = {"products": products}
    return render(request, 'products/index.html', context=context)



# add product view
@login_required
def add_product(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')

    context = {
        'form': form
    }

    return render(request, 'products/add.html', context)



# Update product view
def update_product(request, pk):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return HttpResponse("Product not found", status=404)

    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')

    context = {
        'form': form
    }

    return render(request, 'products/update.html', context)



# Product detail view
def product_detail(request, pk):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return HttpResponse("Product not found", status=404)

    context = {'product': product}
    return render(request, 'products/detail.html', context)


# delete product view
@login_required(login_url='login')
def delete_product(request, pk):
    try:
        product = Product.objects.get(id=pk)
        product.delete()
    except Product.DoesNotExist:
        return HttpResponse("Product not found", status=404)

    return redirect('product_list')



#customer list view
@login_required(login_url='login')
def customer_list(request):
    try:
        customer_list = Customer.objects.all()
    except Customer.DoesNotExist:
        customer_list = []

    context = {
        'customers': customer_list
    }
    return render(request, 'customer/index.html', context)



# Customer detail view
def customer_detail(request, pk):
    try:
        customer = Customer.objects.get(id=pk)
    except Customer.DoesNotExist:
        return HttpResponse("Customer not found", status=404)

    context = {'customer': customer}
    return render(request, 'customer/detail.html', context)


# add customer view
@login_required(login_url='login')
def add_customer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')

    context = {
        'form': form
    }

    return render(request, 'customer/add.html', context)


# Update customer view
@login_required(login_url='login')
def update_customer(request, pk):
    try:
        customer = Customer.objects.get(id=pk)
    except Customer.DoesNotExist:
        return HttpResponse("Customer not found", status=404)

    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')

    context = {
        'form': form
    }

    return render(request, 'customer/update.html', context)



# delete customer view
@login_required(login_url='login')
def delete_customer(request, pk):
    try:
        customer = Customer.objects.get(id=pk)
        customer.delete()
    except Customer.DoesNotExist:
        return HttpResponse("Customer not found", status=404)

    return redirect('customer_list')


# order list view
@login_required(login_url='login')
def order_list(request):
    try:
        orders = Order.objects.all()
    except Order.DoesNotExist:
        orders = []

    context = {
        'orders': orders,
    }
    return render(request, 'order/index.html', context)


# add order view
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

    return render(request, 'order/add.html', context)


# Update order view
@login_required(login_url='login')
def update_order(request, pk):
    try:
        order = Order.objects.get(id=pk)
    except Order.DoesNotExist:
        return HttpResponse("Order not found", status=404)

    form = OrderForm(instance=order)

    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    
    context = {
        'form': form
    }
    return render(request, 'order/update.html', context)


# delete order view
@login_required(login_url='login')
def delete_order(request, pk):
    try:
        order = Order.objects.get(id=pk)
        order.delete()
    except Order.DoesNotExist:
        return HttpResponse("Order not found", status=404)

    return redirect('order_list')