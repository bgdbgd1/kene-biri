from django.db import models
# from .order import Order


class Driver(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
