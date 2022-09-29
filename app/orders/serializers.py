from rest_framework import serializers
from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    """Serializer for Order objects"""

    class Meta:
        model = Order
        exclude = ('created_at', 'updated_at', 'user_id',)
        read_only_fields = ('id', 'order_code', 'unit_price',)
        # depth = 1


class OrderUpdateSerializer(serializers.ModelSerializer):
    """Serializer for Order update"""

    class Meta:
        model = Order
        exclude = ('created_at', 'updated_at', 'user_id',)
        read_only_fields = ('id',
                            'order_code',
                            'unit_price',
                            'user_id',
                            'product_id',)
