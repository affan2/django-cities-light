from ..models import Country, Region, City

import autocomplete_light


class CityAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ('search_names',)
    choices = City.published.get_live_set()

    def choices_for_request(self):
        """
        Return a queryset based on `choices` using options `split_words`,
        `search_fields` and `limit_choices`. Refer to the class-level
        documentation for documentation on each of these options.
        """
        q = self.request.GET.get('q', '')
        choices = City.published.get_live_set(language=self.request.LANGUAGE_CODE).filter(name__icontains=q)

        return choices[0:self.limit_choices]



class RegionAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ('name', 'name_ascii')
    choices = Region.published.get_live_set()

    def choices_for_request(self):
        """
        Return a queryset based on `choices` using options `split_words`,
        `search_fields` and `limit_choices`. Refer to the class-level
        documentation for documentation on each of these options.
        """
        q = self.request.GET.get('q', '')
        choices = Region.published.get_live_set(language=self.request.LANGUAGE_CODE).filter(name__icontains=q)

        return choices[0:self.limit_choices]


class CountryAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ('name', 'name_ascii')
    choices = Country.published.get_live_set()

    def choices_for_request(self):
        """
        Return a queryset based on `choices` using options `split_words`,
        `search_fields` and `limit_choices`. Refer to the class-level
        documentation for documentation on each of these options.
        """
        q = self.request.GET.get('q', '')
        choices = Country.published.get_live_set(language=self.request.LANGUAGE_CODE).filter(name__icontains=q)

        return choices[0:self.limit_choices]

class RestAutocompleteBase(autocomplete_light. AutocompleteRestModel):
    def model_for_source_url(self, url):
        """
        Return the appropriate model for the urls defined by
        cities_light.contrib.restframework.urlpatterns.

        Used by RestChannel.
        """
        if 'city/' in url:
            return City
        elif 'region/' in url:
            return Region
        elif 'country/' in url:
            return Country


class CityRestAutocomplete(RestAutocompleteBase, CityAutocomplete):
    pass


class RegionRestAutocomplete(RestAutocompleteBase, RegionAutocomplete):
    pass


class CountryRestAutocomplete(RestAutocompleteBase, RegionAutocomplete):
    pass
