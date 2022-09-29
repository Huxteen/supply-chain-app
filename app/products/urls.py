
from django.urls import path, include
from products import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.ProductViewSet, basename='products')

app_name = 'products'

urlpatterns = [
    path('', include(router.urls)),
]
