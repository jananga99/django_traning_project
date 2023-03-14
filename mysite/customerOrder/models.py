from django.db import models

from customer.models import Customer


class CustomerOrder(models.Model):
    """
    created : DateTime   -  Customer order created DateTime at the system
    customer : string    -   Customer id of the related customer
    itemCount: int       -   Number of items
    description: string  -   Description
    """
    created = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, related_name='customerOrders', on_delete=models.CASCADE)
    itemCount = models.PositiveIntegerField('Item Count', default=0)
    description = models.CharField('Description', max_length=5000)

    class Meta:
        ordering = ['created']
