from django.shortcuts import render
from rest_framework import viewsets
from .models import Coffee, Order
from .serializers import CoffeeSerializer, OrderSerializer

from .serializers import CoffeeSerializer

def landing_view(request):
    return render(request, 'landing.html')


class CoffeeViewSet(viewsets.ModelViewSet):
    queryset = Coffee.objects.all()  # Correct: use 'objects', not 'object'
    serializer_class = CoffeeSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
