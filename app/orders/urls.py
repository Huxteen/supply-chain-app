
from django.urls import path, include
from orders import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.OrderViewSet, basename='orders')

app_name = 'orders'

urlpatterns = [
    path('', include(router.urls)),
    path('update/<int:pk>',
         views.UpdateOrderView.as_view(),
         name='update-order'),
]
