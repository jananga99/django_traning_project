from rest_framework import serializers
from customer.models import Customer


class CustomerSerializer(serializers.ModelSerializer):

    customerOrders = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = ['id', 'firstName', 'lastName', 'dob', 'currencyBalance', 'pageVisits', 'created', 'customerOrders']