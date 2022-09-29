
from django.urls import path, include
from address import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.AddressViewSet, basename='address')

app_name = 'address'

urlpatterns = [
    path('', include(router.urls)),
]
