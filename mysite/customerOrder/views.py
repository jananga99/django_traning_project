from customerOrder.models import CustomerOrder
from customerOrder.serializers import CustomerOrderSerializer
from rest_framework import generics


class CustomerOrderList(generics.ListCreateAPIView):
    queryset = CustomerOrder.objects.all()
    serializer_class = CustomerOrderSerializer


class CustomerOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomerOrder.objects.all()
    serializer_class = CustomerOrderSerializer
