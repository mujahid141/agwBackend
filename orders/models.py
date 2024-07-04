from django.db import models
from django.contrib.auth.models import User

from products.models import Product

class Order(models.Model):
    PAYMENT_P ='P'
    PAYMENT_C ='C'
    PAYMENT_F ='F'
    PAYMENT_CHOICES = [
        (PAYMENT_P, 'Pending'),
        (PAYMENT_C, 'Complete'),
        (PAYMENT_F, 'Failed'),
    ]
    placed_at = models.DateField(auto_now_add=True)
    customer = models.ForeignKey(User, on_delete=models.PROTECT, related_name='orders')
    payment_status = models.CharField(max_length=1, choices=PAYMENT_CHOICES, default=PAYMENT_P)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='order_items')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=3)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        unique_together = ('order', 'product')

class Cart(models.Model):
    created_at = models.DateField(auto_now_add=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=3)
    
    
class WishList(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name='products')
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name= 'user')
    
    
    def __str__(self) -> str:
        return self.product.title
    
