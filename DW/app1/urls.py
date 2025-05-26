from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('view-two/', views.view_two, name='two'),
    # path('view-three/', views.view_three, name='three'),
    path('view-four/', views.view_four, name='four'),
    path('products/<int:pk>/', views.product, name='product'),  # <-- FIXED LINE
    path('order/<int:pk>/', views.order_product, name='order_product'),
    path('about/', views.about, name='two'),
    path('reviews/', views.reviews, name='five'),
    path('faq/', views.faq, name='four'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)