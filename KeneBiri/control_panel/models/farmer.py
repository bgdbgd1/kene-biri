from django.db import models


class Farmer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    street = models.CharField(max_length=200)
    house_nr = models.IntegerField()
    house_nr_extension = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=30, blank=None, null=None, default=None)
