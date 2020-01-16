from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.Venue)
admin.site.register(models.VenueList)
