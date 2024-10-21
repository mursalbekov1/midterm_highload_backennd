# shop/admin.py
from django.contrib import admin
from .models import Product, Order, OrderItem, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category')  # Здесь category должен быть правильным
    search_fields = ('name',)
    list_filter = ('category',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'total_amount')  # Убедитесь, что поля правильные
    search_fields = ('user__username',)
    # Удалите статус и временные метки, если они не существуют в Order
    # list_filter = ('status', 'created_at')  # Если статус не существует, уберите его
    list_filter = ('created_at',)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')
    search_fields = ('order__user__username', 'product__name')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
