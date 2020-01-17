import json

from django.http import HttpResponse
from django.views import View
from rest_framework import viewsets
from django.views.generic.base import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

from . import models, serializers


class IndexView(View):
    def get(self, request, *args, **kwargs):
        index = json.dumps({
            'venues_url': self.request.build_absolute_uri(reverse('venues')),
            'venues_list_uri': self.request.build_absolute_uri(reverse('venues-list'))
        },  indent=4, sort_keys=True)
        return HttpResponse(index, content_type="application/json")



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
