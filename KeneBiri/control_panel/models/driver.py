from django.db import models
# from .order import Order


class Driver(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=30, blank=None, null=None, default=None)
