from customerOrder.models import CustomerOrder
from customerOrder.serializers import CustomerOrderSerializer
from rest_framework import generics


class CustomerOrderList(generics.ListCreateAPIView):
    """
    This endpoint allows you to retrieve customer orders from the system. You can use this endpoint to retrieve
    customer orders from the system entirely.
    """
    queryset = CustomerOrder.objects.all()
    serializer_class = CustomerOrderSerializer


class CustomerOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    This endpoint allows you to retrieve, update, or delete a specific customer order from the system. You can use
    this endpoint to retrieve the details of a customer prder, update their information, or remove them from the
    system entirely.

    To use this endpoint, you need to provide the ID of the customer order you want to retrieve, update, or delete in
    the URL. The ID should be included at the end of the URL after the slash (/).

    For example, to retrieve the details of a customer order with an ID of 1, you would make a GET request to:

    /orders/1/

    To update the information of the same customer order, you would make a PUT or PATCH request to the same URL. To
    delete the customer order, you would make a DELETE request to the same URL.
    """
    queryset = CustomerOrder.objects.all()
    serializer_class = CustomerOrderSerializer
