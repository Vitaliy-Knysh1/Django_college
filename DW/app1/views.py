from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Product, Order
from .forms import OrderForm

# Create your views here.

def product(request,pk):
	product = Product.objects.get(id=pk)
	return render(request, 'product.html', {'product':product})

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def view_two(request):
    return render(request, 'generic_view.html', {'title': 'View Two', 'heading': 'This is View Two'})

def view_three(request):
    return render(request, 'generic_view.html', {'title': 'View Three', 'heading': 'This is View Three'})

def view_four(request):
    return render(request, 'generic_view.html', {'title': 'View Four', 'heading': 'This is View Four'})

def view_five(request):
    return render(request, 'generic_view.html', {'title': 'View Five', 'heading': 'This is View Five'})

def order_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number_of_items']
            # Only create order if enough stock
            if product.stock >= number:
                Order.objects.create(
                    product=product,
                    number_of_items=number
                )
                product.stock -= number
                product.save()
                return render(request, 'order_success.html', {'product': product})
            else:
                form.add_error('number_of_items', 'Not enough stock available.')
    else:
        form = OrderForm()
    return render(request, 'order_form.html', {'form': form, 'product': product})