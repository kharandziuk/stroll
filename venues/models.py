from django.db import models
from django.urls import reverse

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
    photo = models.FileField(upload_to="uploads/", blank=True)


class VenueList(models.Model):
    slug = models.SlugField(primary_key=True)
    title = models.CharField(
        blank=True,
        max_length=100,
    )
    venues = models.ManyToManyField("venues.Venue", related_name="lists")

    def venues_url(self):
        return reverse('venues-list-venues',kwargs={
            'slug': self.slug
        })
