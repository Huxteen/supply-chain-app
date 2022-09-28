from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

# id, 
# name, 
# price, 
# quantity in stock

class Product(models.Model):
    """Product table"""
    name = models.CharField(max_length=255)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_user_id')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

