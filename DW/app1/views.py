from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Product, Order, Review
from .forms import OrderForm, ReviewForm

# Create your views here.

def product(request, pk):
    product = Product.objects.get(pk=pk)
    product_reviews = product.reviews.order_by('-created_at')
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.save()
            return redirect('product', pk=product.pk)
    else:
        form = ReviewForm()
    return render(request, 'product.html', {
        'product': product,
        'reviews': product_reviews,
        'form': form,
    })

def home(request):
    query = request.GET.get('q', '')
    products = Product.objects.all()
    if query:
        products = products.filter(name__icontains=query)
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

def reviews(request):
    reviews = Review.objects.filter(product__isnull=True).order_by('-created_at')
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('five')
    else:
        form = ReviewForm()
    return render(request, 'reviews.html', {'reviews': reviews, 'form': form})

def about(request):
    return render(request, 'about.html')

def faq(request):
    return render(request, 'faq.html')