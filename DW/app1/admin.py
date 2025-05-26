from django.contrib import admin

from .models import Category, Product, Order

admin.site.register(Category)
admin.site.register(Product)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'number_of_items', 'first_name', 'last_name', 'email', 'card_number', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'card_number', 'product__name')

admin.site.register(Order, OrderAdmin)
