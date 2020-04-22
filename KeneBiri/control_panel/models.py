from django.db import models

# Create your models here.


class Farmer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    street = models.CharField(max_length=200)
    house_nr = models.IntegerField()
    house_nr_extension = models.IntegerField()
    zipcode = models.CharField(max_length=10)


class Driver(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Orders(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.SET_NULL, null=True)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)
    liters_of_milk = models.IntegerField()
    production_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    fulfilled = models.BooleanField(default=False)
