from django.contrib import admin
from .models import Cart, Order, OrderItem

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'meal', 'quantity', 'created_at', 'total_price')
    list_filter = ('created_at', 'user')
    search_fields = ('user__username', 'meal__name')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_amount', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at', 'user')
    search_fields = ('user__username',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'meal', 'quantity')
    list_filter = ('order',)
    search_fields = ('meal__name',)