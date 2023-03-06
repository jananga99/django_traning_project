from django.core.validators import MinValueValidator
from django.db import models


class Customer(models.Model):
    firstName = models.CharField('First Name', max_length=200)
    lastName = models.CharField('Last Name', max_length=200)
    dob = models.DateField('Date of Birth')
    currencyBalance = models.FloatField('Currency Balance', default=0)
    pageVisits = models.IntegerField('Page Visits', default=0, validators=[MinValueValidator(0)])
