from django.conf.urls import re_path

from .autocomplete_views import *

urlpatterns = [
    re_path(r'^city-autocomplete/$', CityAutocomplete.as_view(), name='city-autocomplete', ),
    re_path(r'^region-autocomplete/$', RegionAutocomplete.as_view(), name='region-autocomplete', ),
    re_path(r'^country-autocomplete/$', CountryAutocomplete.as_view(), name='country-autocomplete', ),
]
