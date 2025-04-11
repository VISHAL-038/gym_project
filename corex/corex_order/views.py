from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cart, Order, OrderItem
from corex_diet.models import Meal

@login_required
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.total_price() for item in cart_items)
    return render(request, 'corex_order/cart.html', {'cart_items': cart_items, 'total': total})

@login_required
def add_to_cart(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, meal=meal)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    messages.success(request, f"Added {meal.name} to cart!")
    return redirect('diet_tracking')  # Redirect back to diet tracking page

@login_required
def remove_from_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)
    cart_item.delete()
    messages.success(request, "Item removed from cart!")
    return redirect('cart')

@login_required
def create_order(request):
    cart_items = Cart.objects.filter(user=request.user)
    if not cart_items.exists():
        messages.error(request, "Your cart is empty!")
        return redirect('cart')
    
    total_amount = sum(item.total_price() for item in cart_items)
    order = Order.objects.create(user=request.user, total_amount=total_amount)
    for item in cart_items:
        OrderItem.objects.create(order=order, meal=item.meal, quantity=item.quantity)
    cart_items.delete()
    messages.success(request, f"Order #{order.id} created successfully!")
    return redirect('order_history')

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'corex_order/order_history.html', {'orders': orders})