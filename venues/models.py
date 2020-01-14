from django.db import models

# Create your models here.

class Venue(models.Model):
    title = models.CharField(
        blank=True,
        max_length=100,
    )
    description = models.CharField(
        blank=True,
        max_length=100,
    )
    opening_times = models.CharField(
        blank=True,
        max_length=100,
    )
    address = models.CharField(
        blank=True,
        max_length=100,
    )
    other = models.CharField(
        blank=True,
        max_length=100,
    )
    category = models.CharField(
        blank=True,
        max_length=100,
    )
