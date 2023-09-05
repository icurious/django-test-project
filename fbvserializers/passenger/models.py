from django.db import models

# Create your models here.

class Passengers(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    travel_points= models.CharField(max_length=255)