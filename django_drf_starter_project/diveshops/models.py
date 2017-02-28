from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator



# models for store based data
class Store(models.Model):
    """ Store location model."""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100,default='none')
    location = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    address = models.CharField(max_length=1000)
    opening_date = models.DateTimeField(default=timezone.now)
    website = models.URLField(max_length=500)
    founded_date = models.CharField(max_length=500)

    # Business hours in a 24 hour clock.  Default 8am-5pm.
    business_hours_start = models.IntegerField(
        default=8,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(23)
        ]
    )
    business_hours_end = models.IntegerField(
        default=17,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(23)
        ]
    )
class StorePrices(models.Model):
    store = models.ForeignKey(Store)

class DiveLocation(models.Model):
    location_name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
