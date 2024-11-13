from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CoffeeViewSet, OrderViewSet
from .views import landing_view

router = DefaultRouter()
router.register(r'coffees', CoffeeViewSet)
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    # path('', landing_view, name='landing'),
    path('', include(router.urls))
]
