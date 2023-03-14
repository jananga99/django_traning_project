from customer.models import Customer
from customer.serializers import CustomerSerializer
from rest_framework import generics
from auth.authentication import BearerAuthentication
from auth.authentication import IsAuthenticatedSub


class CustomerList(generics.ListCreateAPIView):
    """
    Retrieves customers or create customer if authenticated.
    To retrieve all customers , GET request is to be made to /customers/.
    To retrieve a customer , POST request is to be made to /customers/.
    """
    authentication_classes = [BearerAuthentication]
    permission_classes = [IsAuthenticatedSub]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieves, updates or deletes a specific customer if authenticated.
    To retrieve a customer with an ID of 1, GET request is to be made to /customers/1/.
    To update, PUT or PATCH is to be used.
    To delete, DELETE is to be used.
    """
    authentication_classes = [BearerAuthentication]
    permission_classes = [IsAuthenticatedSub]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
