from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.http import JsonResponse
from products import serializers
from products.paginations import CustomPagination
from products.models import Product


# Create your views here.
class ProductViewSet(viewsets.GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,):
    """Manage data in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all().order_by('id')
    serializer_class = serializers.ProductSerializer
    pagination_class = CustomPagination

    def get_permissions(self):
        if ((self.action).lower()) in ['create', 'update', 'partial_update']:
            permission_classes = (IsAuthenticated, IsAdminUser,)
        else:
            permission_classes = (IsAuthenticated,)
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        """Create new Product"""
        serializer.save(user_id=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return JsonResponse(serializer.data)
