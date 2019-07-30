# -*- encoding: utf-8 -*-


from django import test

from ..forms import CountryForm, CityForm
from ..models import Country, City


class FormTestCase(test.TransactionTestCase):
    reset_sequences = True

    def testCountryFormNameAndContinentAlone(self):
        form = CountryForm({'name': 'Spain', 'continent': 'E'})
        self.assertTrue(form.is_valid())
        form.save()

    def testCityFormNameAndCountryAlone(self):
        country = Country(name='France')
        country.save()
        form = CityForm({'name': 'Paris', 'country': country.pk})
        self.assertTrue(form.is_valid())
        form.save()


class SaveTestCase(test.TransactionTestCase):
    reset_sequences = True

    def testCountryAsciiAndSlug(self):
        country = Country(name='áó éú', geoname_id=1)
        country.save()

        self.assertEqual(country.name_ascii, 'ao e')
        self.assertEqual(country.slug, 'ao-e')

    def testCityAsciiAndSlug(self):
        country = Country(name='Belgium', geoname_id=2802361)
        country.save()

        city = City(name='áó éú', country=country, geoname_id=2)
        city.save()

        self.assertEqual(city.name_ascii, 'ao e')
        self.assertEqual(city.slug, 'ao-e')
