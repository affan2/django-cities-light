from __future__ import unicode_literals

from django import forms

from .models import Country, Region, City
from hvad.forms import TranslatableModelForm

__all__ = ['CountryForm', 'RegionForm', 'CityForm']


class CountryForm(TranslatableModelForm):
    """
    Country model form.
    """
    class Meta:
        model = Country
        exclude = ('name_ascii', 'slug', 'geoname_id')


class RegionForm(TranslatableModelForm):
    """
    Region model form.
    """
    class Meta:
        model = Region
        exclude = ('name_ascii', 'slug', 'geoname_id', 'display_name',
                   'geoname_code')


class CityForm(TranslatableModelForm):
    """
    City model form.
    """
    class Meta:
        model = City
        exclude = ('name_ascii', 'search_names', 'slug', 'geoname_id',
                   'display_name', 'feature_code')
