from copy import copy

from django.contrib import admin
from django.contrib.admin.views.main import ChangeList

from .forms import *
from .abstract_models import to_search
from .loading import get_cities_models

from general.admin import CustomTranslatableAdmin

Country, Region, City = get_cities_models()


class CountryAdmin(CustomTranslatableAdmin):
    """
    ModelAdmin for Country.
    """

    list_display = (
        'name_',
        'code2',
        'code3',
        'continent',
        'tld',
        'phone',
        'geoname_id',
    )
    search_fields = (
        'name_',
        'name_ascii',
        'code2',
        'code3',
        'tld',
        'geoname_id',
    )
    list_filter = (
        'continent',
    )
    form = CountryForm


admin.site.register(Country, CountryAdmin)


class RegionAdmin(CustomTranslatableAdmin):
    """
    ModelAdmin for Region.
    """
    list_filter = (
        'country__continent',
        'country',
    )
    search_fields = (
        'name_',
        'name_ascii',
        'geoname_id',
    )
    list_display = (
        'name_',
        'get_country',
        'geoname_id',
    )
    form = RegionForm

    def get_country(self, obj):
        return obj.country


admin.site.register(Region, RegionAdmin)


class CityChangeList(ChangeList):
    def get_queryset(self, request):
        if 'q' in list(request.GET.keys()):
            request.GET = copy(request.GET)
            request.GET['q'] = to_search(request.GET['q'])
        return super(CityChangeList, self).get_queryset(request)


class CityAdmin(CustomTranslatableAdmin):
    """
    ModelAdmin for City.
    """
    list_display = (
        'name_',
        'get_region',
        'get_country',
        'geoname_id',
        'timezone'
    )
    search_fields = (
        'search_names',
        'geoname_id',
        'timezone'
    )
    list_filter = (
        'country__continent',
        'country',
        'timezone'
    )
    form = CityForm

    def get_changelist(self, request, **kwargs):
        return CityChangeList

    def get_region(selfs, obj):
        return obj.region
    get_region.short_description = 'region'

    def get_country(self, obj):
        return obj.country
    get_country.short_description = 'country'


admin.site.register(City, CityAdmin)
