from customer.models import Customer
from customer.serializers import CustomerSerializer
from rest_framework import generics


class CustomerList(generics.ListCreateAPIView):
    """
    This endpoint allows you to retrieve customers from the system. You can use this endpoint to retrieve customers
    from the system entirely.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    This endpoint allows you to retrieve, update, or delete a specific customer from the system. You can use this
    endpoint to retrieve the details of a customer, update their information, or remove them from the system entirely.

    To use this endpoint, you need to provide the ID of the customer you want to retrieve, update, or delete in the URL.
    The ID should be included at the end of the URL after the slash (/).

    For example, to retrieve the details of a customer with an ID of 1, you would make a GET request to:

    /customers/1/

    To update the information of the same customer, you would make a PUT or PATCH request to the same URL. To delete
    the customer, you would make a DELETE request to the same URL.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
