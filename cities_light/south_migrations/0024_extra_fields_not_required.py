# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Deleting field 'City.display_name'
        db.delete_column(u'cities_light_city', 'display_name')

        # Deleting field 'City.name'
        db.delete_column(u'cities_light_city', 'name')


        # Deleting field 'Country.name'
        db.delete_column(u'cities_light_country', 'name')

        # Deleting field 'Region.display'
        db.delete_column(u'cities_light_region', 'name')

        # Deleting field 'Region.display_name'
        db.delete_column(u'cities_light_region', 'display_name')

    def backwards(self, orm):
        pass