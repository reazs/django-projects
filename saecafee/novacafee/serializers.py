from rest_framework import serializers
from .models import Coffee, Order
class CoffeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coffee
        fields = '__all__'
        

class OrderSerializer(serializers.ModelSerializer):
    # Display the coffee details in the response
    coffee = CoffeeSerializer(read_only=True)
    # Accept coffee_id as input for creating/updating orders
    coffee_id = serializers.PrimaryKeyRelatedField(
        queryset=Coffee.objects.all(), source='coffee', write_only=True
    )

    class Meta:
        model = Order
        fields = ['id', 'customer_name', 'coffee', 'coffee_id', 'quantity', 'status', 'created_at']

    def create(self, validated_data):
        # Extract the coffee instance using 'coffee_id'
        coffee = validated_data.pop('coffee')
        return Order.objects.create(coffee=coffee, **validated_data)

    def update(self, instance, validated_data):
        # Extract the coffee instance using 'coffee_id' if provided
        if 'coffee' in validated_data:
            instance.coffee = validated_data.pop('coffee')
        return super().update(instance, validated_data)