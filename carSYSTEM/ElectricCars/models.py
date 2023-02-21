from django.db import models

# Create your models here.

class Car(models.Model):
    brand = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    colour = models.CharField()
    miles_range = models.IntegerField()
    date_of_creation = models.DateField()