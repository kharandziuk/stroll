from django.urls import path
from django.contrib import admin
from rest_framework import routers
from . import views
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    path('venues',
        views.VenueViewSet.as_view(dict(get='list', post='create')),
        name='venues'
    ),
    path('lists',
        views.VenuesListViewSet.as_view(dict(get='list', post='create')),
        name='venues'
    ),
    path(
        'lists/<slug:slug>/venues',
        views.VenueListVenuesForwardView.as_view(),
        name='venues-list-venues'
    )
]

urlpatterns = format_suffix_patterns(urlpatterns)
