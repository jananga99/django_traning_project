from rest_framework import serializers
from customerOrder.models import CustomerOrder


class CustomerOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerOrder
        fields = ['id', 'itemCount','description', 'created', 'customer']
