

from django import forms

from .loading import get_cities_models

from hvad.forms import TranslatableModelForm

Country, Region, City = get_cities_models()

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
