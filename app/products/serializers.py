from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for Product objects"""
    
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'quantity_in_stock')
        read_only_fields = ('id',)
        
    