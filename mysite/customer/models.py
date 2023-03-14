from django.core.validators import MinValueValidator
from django.db import models


class Customer(models.Model):
    """
    created : DateTime      -   Customer created DateTime at the system
    firstName : string      -   First name of the customer
    lastName : string       -   lastname of the customer
    dob : Date              -   Date of birthday of the customer
    currencyBalance : float -   Currency balance in dollars
    pageVisits : int        -   Number of page visits
    """
    created = models.DateTimeField(auto_now_add=True)
    firstName = models.CharField('First Name', max_length=200)
    lastName = models.CharField('Last Name', max_length=200)
    dob = models.DateField('Date of Birth')
    currencyBalance = models.FloatField('Currency Balance', default=0)
    pageVisits = models.IntegerField('Page Visits', default=0, validators=[MinValueValidator(0)])

    class Meta:
        ordering = ['created']