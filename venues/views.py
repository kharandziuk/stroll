from rest_framework import viewsets

from . import models, serializers

class VenueViewSet(viewsets.ModelViewSet):
    queryset = models.Venue.objects.all()
    serializer_class = serializers.VenueSerializer
