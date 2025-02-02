import autoslug
import six
import re

from django.conf import settings
from django.db.models import signals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _

from unidecode import unidecode

from .settings import *

from general.constants import STATE_TYPES
from general.managers import TranslateEntityManager, CustomEntityManager
from general.fields import CustomTranslatedFields
from hvad.models import TranslatableModel

__all__ = ['Country', 'Region', 'City', 'CONTINENT_CHOICES', 'to_search', 'to_ascii']

ALPHA_REGEXP = re.compile('[\W_]+', re.UNICODE)

CONTINENT_CHOICES = (
    ('OC', _('Oceania')),
    ('EU', _('Europe')),
    ('AF', _('Africa')),
    ('NA', _('North America')),
    ('AN', _('Antarctica')),
    ('SA', _('South America')),
    ('AS', _('Asia')),
)


def to_ascii(value):
    if not six.PY3 and isinstance(value, str):
        value = force_text(value)

    return unidecode(value)


def to_search(value):
    """
    Convert a string value into a string that is usable against
    City.search_names.

    For example, 'Paris Texas' would become 'paristexas'.
    """

    return ALPHA_REGEXP.sub('', to_ascii(value)).lower()


def set_name_ascii(sender, instance=None, **kwargs):
    """
    Signal reciever that sets instance.name_ascii from instance.name.

    Ascii versions of names are often useful for autocompletes and search.
    """
    name_ascii = to_ascii(instance.name)

    if not name_ascii.strip():
        return

    if name_ascii and not instance.name_ascii:
        instance.name_ascii = to_ascii(instance.name)


def set_display_name(sender, instance=None, **kwargs):
    """
    Set instance.display_name to instance.get_display_name(), avoid spawning
    queries during __str__().
    """
    instance.display_name = instance.get_display_name()


@python_2_unicode_compatible
class Base(models.Model):
    """
    Base model with boilerplate for all models.
    """

    name_ascii = models.CharField(max_length=200, blank=True, db_index=True)
    slug = autoslug.AutoSlugField(populate_from='name_ascii')
    geoname_id = models.IntegerField(null=True, blank=True, unique=True)
    alternate_names = models.TextField(null=True, blank=True, default='')
    state = models.SmallIntegerField(verbose_name=_('Publish state'), choices=STATE_TYPES, default=1)
    default_language = models.CharField(max_length=2, choices=settings.LANGUAGES, default='en', verbose_name=_('Default language'))

    class Meta:
        abstract = True
        # ordering = ['name']

    def __str__(self):
        display_name = getattr(self, 'display_name', None)
        if display_name:
            return display_name
        return self.name


class Country(Base, TranslatableModel):
    """
    Country model.
    """
    translations = CustomTranslatedFields(
        name=models.CharField(
            max_length=200
        ),
        source_language=models.CharField(
            max_length=2,
            choices=settings.LANGUAGES,
            default='en',
            verbose_name=_('Source language')
        ),
        is_auto_translated=models.BooleanField(
            verbose_name=_('Auto Translated'),
            default=False
        ),
        meta={'unique_together': [('name', 'language_code', 'master')]},
    )

    code2 = models.CharField(max_length=2, null=True, blank=True, unique=True)
    code3 = models.CharField(max_length=3, null=True, blank=True, unique=True)
    continent = models.CharField(max_length=2, db_index=True,
        choices=CONTINENT_CHOICES)
    tld = models.CharField(max_length=5, blank=True, db_index=True)
    phone = models.CharField(max_length=20, null=True)

    allow_translate = models.BooleanField(verbose_name=_('Allow Translate'), default=True)

    objects = CustomEntityManager()
    published = TranslateEntityManager()

    class Meta(Base.Meta):
        verbose_name_plural = _('countries')

    @property
    def name_(self):
        return self.name

    def __str__(self):
        return self.name

signals.pre_save.connect(set_name_ascii, sender=Country)



class Region(Base, TranslatableModel):
    """
    Region/State model.
    """
    translations = CustomTranslatedFields(
        name=models.CharField(
            max_length=200
        ),
        display_name=models.CharField(
            max_length=200
        ),
        source_language=models.CharField(
            max_length=2,
            choices=settings.LANGUAGES,
            default='en',
            verbose_name=_('Source language')
        ),
        is_auto_translated=models.BooleanField(
            verbose_name=_('Auto Translated'),
            default=False
        ),
        meta={'unique_together': [('name', 'language_code', 'master')]},
    )

    geoname_code = models.CharField(max_length=50, null=True, blank=True,db_index=True)
    country = models.ForeignKey(Country)
    allow_translate = models.BooleanField(verbose_name=_('Allow Translate'), default=True)

    objects = CustomEntityManager()
    published = TranslateEntityManager()

    class Meta(Base.Meta):
        unique_together = (('country', 'slug'))
        verbose_name = _('region/state')
        verbose_name_plural = _('regions/states')

    @property
    def name_(self):
        return self.name

    def get_display_name(self):
        return '%s, %s' % (self.name, self.country.name)

signals.pre_save.connect(set_name_ascii, sender=Region)
signals.pre_save.connect(set_display_name, sender=Region)


class ToSearchTextField(models.TextField):
    """
    Trivial TextField subclass that passes values through to_search
    automatically.
    """
    def get_prep_lookup(self, lookup_type, value):
        """
        Return the value passed through to_search().
        """
        value = super(ToSearchTextField, self).get_prep_lookup(lookup_type,
            value)
        return to_search(value)

    def south_field_triple(self):
        "Returns a suitable description of this field for South."
        from south.modelsinspector import introspector
        field_class = self.__class__.__module__ + "." + self.__class__.__name__
        args, kwargs = introspector(self)
        # That's our definition!
        return (field_class, args, kwargs)


class City(Base, TranslatableModel):
    """
    Region/State model.
    """
    translations = CustomTranslatedFields(
        name=models.CharField(
            max_length=200,
            db_index=True
        ),
        display_name=models.CharField(
            max_length=200
        ),
        source_language=models.CharField(
            max_length=2,
            choices=settings.LANGUAGES,
            default='en',
            verbose_name=_('Source language')
        ),
        is_auto_translated=models.BooleanField(
            verbose_name=_('Auto Translated'),
            default=False
        ),
        meta={'unique_together': [('name', 'language_code', 'master')]},
    )

    search_names = ToSearchTextField(max_length=4000, db_index=INDEX_SEARCH_NAMES, blank=True, default='')

    latitude = models.DecimalField(max_digits=8, decimal_places=5, null=True, blank=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=5, null=True, blank=True)

    region = models.ForeignKey(Region, blank=True, null=True)
    country = models.ForeignKey(Country)
    population = models.BigIntegerField(null=True, blank=True, db_index=True)
    feature_code = models.CharField(max_length=10, null=True, blank=True, db_index=True)

    allow_translate = models.BooleanField(verbose_name=_('Allow Translate'), default=True)

    objects = CustomEntityManager()
    published = TranslateEntityManager()

    class Meta(Base.Meta):
        unique_together = (('region', 'slug'))
        verbose_name_plural = _('cities')

    @property
    def name_(self):
        return self.name

    def get_display_name(self):
        if self.region_id:
            try:
                return '%s, %s, %s' % (self.name, self.region.name, self.country.name)
            except:
                return '%s, %s' % (self.name, self.country.name)
        else:
            return '%s, %s' % (self.name, self.country.name)

signals.pre_save.connect(set_name_ascii, sender=City)
signals.pre_save.connect(set_display_name, sender=City)


def city_country(sender, instance, **kwargs):
    if instance.region_id and not instance.country_id:
        instance.country = instance.region.country
signals.pre_save.connect(city_country, sender=City)


def city_search_names(sender, instance, **kwargs):
    search_names = []

    country_names = [instance.country.name]
    if instance.country.alternate_names:
        country_names += instance.country.alternate_names.split(',')

    city_names = [instance.name]
    if instance.alternate_names:
        city_names += instance.alternate_names.split(',')

    try:
        instance.region.name
        regoin_flag = True
    except:
        regoin_flag = False

    if instance.region_id and regoin_flag:
        region_names = [instance.region.name]
        if instance.region.alternate_names:
            region_names += instance.region.alternate_names.split(',')

    for city_name in city_names:
        for country_name in country_names:
            name = to_search(city_name + country_name)
            if name not in search_names:
                search_names.append(name)

            if instance.region_id and regoin_flag:
                for region_name in region_names:
                    name = to_search(city_name + region_name + country_name)
                    if name not in search_names:
                        search_names.append(name)

    instance.search_names = ' '.join(search_names)
signals.pre_save.connect(city_search_names, sender=City)
