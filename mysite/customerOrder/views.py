from customerOrder.models import CustomerOrder
from customerOrder.serializers import CustomerOrderSerializer
from rest_framework import generics
from auth.authentication import BearerAuthentication
from auth.authentication import IsAuthenticatedSub


class CustomerOrderList(generics.ListCreateAPIView):
    """
    Retrieves customer orders or create customer order if authenticated.
    To retrieve all customer orders , GET request is to be made to /orders/.
    To retrieve a customer order , POST request is to be made to /orders/.
    """
    authentication_classes = [BearerAuthentication]
    permission_classes = [IsAuthenticatedSub]
    queryset = CustomerOrder.objects.all()
    serializer_class = CustomerOrderSerializer


class CustomerOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieves, updates or deletes a specific customer order if authenticated.
    To retrieve a customer order with an ID of 1, GET request is to be made to /orders/1.
    To update, PUT or PATCH is to be used.
    To delete, DELETE is to be used.
    """
    authentication_classes = [BearerAuthentication]
    permission_classes = [IsAuthenticatedSub]
    queryset = CustomerOrder.objects.all()
    serializer_class = CustomerOrderSerializer
