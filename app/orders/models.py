from django.db import models
from products.models import Product
from address.models import Address
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Order(models.Model):
    """Order table"""
    order_code = models.CharField(max_length=255, unique=True)
    status = models.BooleanField(default=False)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_product_id')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_user_id')
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='order_address_id')
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    note = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.order_code
