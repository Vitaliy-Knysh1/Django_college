from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator


# Create your views here.

def home(request):
    return render(request, 'base.html')

def view_two(request):
    return render(request, 'generic_view.html', {'title': 'View Two', 'heading': 'This is View Two'})

def view_three(request):
    return render(request, 'generic_view.html', {'title': 'View Three', 'heading': 'This is View Three'})

def view_four(request):
    return render(request, 'generic_view.html', {'title': 'View Four', 'heading': 'This is View Four'})

def view_five(request):
    return render(request, 'generic_view.html', {'title': 'View Five', 'heading': 'This is View Five'})