from rest_framework import serializers
from address.models import Address


class AddressSerializer(serializers.ModelSerializer):
    """Serializer for Address objects"""

    class Meta:
        model = Address
        read_only_fields = ('id',)
        exclude = ('created_at', 'updated_at', 'user_id',)
