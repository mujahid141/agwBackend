from django.urls import path
from .views import OrderView, OrderItemView, CartView, CartItemView, WishListView

urlpatterns = [
    # Order URLs
    path('orders/', OrderView.as_view(), name='order_list'),
    path('orders/<int:pk>/', OrderView.as_view(), name='order_detail'),
    path('orders/create/', OrderView.as_view(), name='order_create'),
    path('orders/<int:pk>/update/', OrderView.as_view(), name='order_update'),
    path('orders/<int:pk>/delete/', OrderView.as_view(), name='order_delete'),

    # Order Item URLs
    path('order-items/', OrderItemView.as_view(), name='order_item_list'),
    path('order-items/<int:pk>/', OrderItemView.as_view(), name='order_item_detail'),
    path('order-items/create/', OrderItemView.as_view(), name='order_item_create'),
    path('order-items/<int:pk>/update/', OrderItemView.as_view(), name='order_item_update'),
    path('order-items/<int:pk>/delete/', OrderItemView.as_view(), name='order_item_delete'),

    # Cart URLs
    path('carts/', CartView.as_view(), name='cart_list'),
    path('carts/<int:pk>/', CartView.as_view(), name='cart_detail'),
    path('carts/create/', CartView.as_view(), name='cart_create'),
    path('carts/<int:pk>/update/', CartView.as_view(), name='cart_update'),
    path('carts/<int:pk>/delete/', CartView.as_view(), name='cart_delete'),

    # Cart Item URLs
    path('cart-items/', CartItemView.as_view(), name='cart_item_list'),
    path('cart-items/<int:pk>/', CartItemView.as_view(), name='cart_item_detail'),
    path('cart-items/create/', CartItemView.as_view(), name='cart_item_create'),
    path('cart-items/<int:pk>/update/', CartItemView.as_view(), name='cart_item_update'),
    path('cart-items/<int:pk>/delete/', CartItemView.as_view(), name='cart_item_delete'),
    
    #wishlist

    path('wishlist/<int:user>/', WishListView.as_view(), name='wishlist'),
    
]