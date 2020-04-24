from django.db import models

from .farmer import Farmer
from .driver import Driver


class Order(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.SET_NULL, null=True)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True)
    liters_of_milk = models.IntegerField()
    production_time = models.DateTimeField()
    arrival_time = models.DateTimeField(null=True, blank=True)
