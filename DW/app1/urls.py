from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('view-two/', views.view_two, name='two'),
    path('view-three/', views.view_three, name='three'),
    path('view-four/', views.view_four, name='four'),
    path('view-five/', views.view_five, name='five'),
    path('products/', views.product_list, name='product_list'),
]
# This code defines the URL patterns for the app1 Django application.
