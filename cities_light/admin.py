from __future__ import unicode_literals

from copy import copy

from django.contrib import admin
from django.contrib.admin.views.main import ChangeList

from .forms import *
from .models import *
from .settings import *
from general.admin import CustomTranslatableAdmin


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
    )
    search_fields = (
        'name_ascii',
        'code2',
        'code3',
        'tld'
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
    )
    list_display = (
        'name_',
        'country',
    )
    form = RegionForm
admin.site.register(Region, RegionAdmin)


class CityChangeList(ChangeList):
    def get_query_set(self, request):
        if 'q' in list(request.GET.keys()):
            request.GET = copy(request.GET)
            request.GET['q'] = to_search(request.GET['q'])
        return super(CityChangeList, self).get_query_set(request)
    # Django 1.8 compat
    get_queryset = get_query_set


class CityAdmin(CustomTranslatableAdmin):
    """
    ModelAdmin for City.
    """
    list_display = (
        'name_',
        'region',
        'country',
    )
    search_fields = (
        'search_names',
    )
    list_filter = (
        'country__continent',
        'country',
    )
    form = CityForm

    def get_changelist(self, request, **kwargs):
        return CityChangeList

    def save_model(self, request, obj, form, change):
        """
        Given a model instance save it to the database.
        """
        try:
            translated_obj = obj.translations.get(language_code=obj.default_language)
        except:
            translated_obj = obj.translate(obj.default_language)
        translated_obj.name = obj.name
        translated_obj.display_name = obj.display_name
        translated_obj.save()
        obj.save()

admin.site.register(City, CityAdmin)
