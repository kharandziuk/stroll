from rest_framework import viewsets
from django.views.generic.base import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from . import models, serializers

class VenueViewSet(viewsets.ModelViewSet):
    queryset = models.Venue.objects.all()
    serializer_class = serializers.VenueSerializer


    def get_queryset(self):
        queryset = super().get_queryset()
        list_slug= self.request.query_params.get('list', None)
        if list_slug:
            queryset = queryset.filter(lists__slug=list_slug)
        return queryset

class VenuesListViewSet(viewsets.ModelViewSet):
    queryset = models.VenueList.objects.all()
    serializer_class = serializers.VenueListSerializer

class VenueListVenuesForwardView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        request.GET = request.GET.copy()
        request.GET['list'] = kwargs.get('slug')
        return VenueViewSet.as_view(dict(get='list', post='create'))(request)
