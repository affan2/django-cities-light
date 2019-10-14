from django.urls import re_path, path

from .autocomplete_views import *

urlpatterns = [
    path(
        'city-autocomplete',
        CityAutocomplete.as_view(),
        name='city-autocomplete',
    ),
    path(
        'region-autocomplete',
        RegionAutocomplete.as_view(),
        name='region-autocomplete',
    ),
    path(
        'country-autocomplete',
        CountryAutocomplete.as_view(),
        name='country-autocomplete',
    ),
]
