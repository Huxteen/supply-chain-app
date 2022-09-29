from rest_framework import viewsets, mixins, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from orders import serializers
from orders.paginations import CustomPagination
from orders.models import Order
from products.models import Product
from orders.exceptions import ProductOutOfStockValidation
import uuid


# Create your views here.
class OrderViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
                   mixins.CreateModelMixin, mixins.RetrieveModelMixin,):

    """Manage data in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Order.objects.all().order_by('id')
    serializer_class = serializers.OrderSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        return Order.objects.filter(user_id=self.request.user).order_by('id')

    def perform_create(self, serializer):
        """"Create new Order"""
        product_id = self.request.POST.get('product_id')
        quantity = self.request.POST.get('quantity')
        product = Product.objects.get(pk=product_id)
        quantity_in_stock = ((product.quantity_in_stock) - int(quantity))
        if quantity_in_stock < 0:
            raise ProductOutOfStockValidation()

        serializer.save(
            user_id=self.request.user,
            unit_price=product.price,
            order_code=generate_order_code(),
            status=True,
        )

        product = Product.objects.get(pk=product_id)
        product.quantity_in_stock = quantity_in_stock
        product.save()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return JsonResponse(serializer.data)


class UpdateOrderView(generics.UpdateAPIView):
    """Manage data in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.OrderUpdateSerializer
    queryset = Order.objects.all().order_by('id')
    lookup_field = 'pk'

    def perform_update(self, serializer):
        """Create new Order"""
        order_id = self.kwargs['pk']
        quantity = int(self.request.POST.get('quantity'))
        product_id = self.request.POST.get('product_id')
        order = Order.objects.get(pk=order_id)
        product = Product.objects.get(pk=product_id)
        prev_quantity = int(order.quantity)

        if quantity != prev_quantity:
            diff_quantity = quantity - prev_quantity
            quantity_in_stock = ((product.quantity_in_stock) - diff_quantity)
            if quantity_in_stock < 0:
                raise ProductOutOfStockValidation()

            product.quantity_in_stock = quantity_in_stock
            product.save()

        serializer.save()


def generate_order_code():
    data_uuid = uuid.uuid4()
    return data_uuid
