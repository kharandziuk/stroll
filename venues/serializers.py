from rest_framework import serializers

from . import models



class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Venue
        fields = (
            'title',
            'description',
            'opening_times',
            'address',
            'other',
            'category',
        )


class VenueListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VenueList
        fields = (
            'slug',
            'title',
            'venues_url'
        )

