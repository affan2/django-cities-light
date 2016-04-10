# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CountryTranslation'
        db.create_table(u'cities_light_country_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['cities_light.Country'])),
        ))
        db.send_create_signal(u'cities_light', ['CountryTranslation'])

        # Adding unique constraint on 'CountryTranslation', fields ['name', 'language_code', 'master']
        db.create_unique(u'cities_light_country_translation', ['name', 'language_code', 'master_id'])

        # Adding unique constraint on 'CountryTranslation', fields ['language_code', 'master']
        db.create_unique(u'cities_light_country_translation', ['language_code', 'master_id'])

        # Adding model 'Country'
        db.create_table(u'cities_light_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name_ascii', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=200, blank=True)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=(), max_length=50, populate_from='name_ascii')),
            ('geoname_id', self.gf('django.db.models.fields.IntegerField')(unique=True, null=True, blank=True)),
            ('alternate_names', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.SmallIntegerField')(default=1)),
            ('default_language', self.gf('django.db.models.fields.CharField')(default='en', max_length=2)),
            ('code2', self.gf('django.db.models.fields.CharField')(max_length=2, unique=True, null=True, blank=True)),
            ('code3', self.gf('django.db.models.fields.CharField')(max_length=3, unique=True, null=True, blank=True)),
            ('continent', self.gf('django.db.models.fields.CharField')(max_length=2, db_index=True)),
            ('tld', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=5, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
        ))
        db.send_create_signal(u'cities_light', ['Country'])

        # Adding model 'RegionTranslation'
        db.create_table(u'cities_light_region_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['cities_light.Region'])),
        ))
        db.send_create_signal(u'cities_light', ['RegionTranslation'])

        # Adding unique constraint on 'RegionTranslation', fields ['name', 'language_code', 'master']
        db.create_unique(u'cities_light_region_translation', ['name', 'language_code', 'master_id'])

        # Adding unique constraint on 'RegionTranslation', fields ['language_code', 'master']
        db.create_unique(u'cities_light_region_translation', ['language_code', 'master_id'])

        # Adding model 'Region'
        db.create_table(u'cities_light_region', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name_ascii', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=200, blank=True)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=(), max_length=50, populate_from='name_ascii')),
            ('geoname_id', self.gf('django.db.models.fields.IntegerField')(unique=True, null=True, blank=True)),
            ('alternate_names', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.SmallIntegerField')(default=1)),
            ('default_language', self.gf('django.db.models.fields.CharField')(default='en', max_length=2)),
            ('geoname_code', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=50, null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cities_light.Country'])),
        ))
        db.send_create_signal(u'cities_light', ['Region'])

        # Adding unique constraint on 'Region', fields ['country', 'slug']
        db.create_unique(u'cities_light_region', ['country_id', 'slug'])

        # Adding model 'CityTranslation'
        db.create_table(u'cities_light_city_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, db_index=True)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['cities_light.City'])),
        ))
        db.send_create_signal(u'cities_light', ['CityTranslation'])

        # Adding unique constraint on 'CityTranslation', fields ['name', 'language_code', 'master']
        db.create_unique(u'cities_light_city_translation', ['name', 'language_code', 'master_id'])

        # Adding unique constraint on 'CityTranslation', fields ['language_code', 'master']
        db.create_unique(u'cities_light_city_translation', ['language_code', 'master_id'])

        # Adding model 'City'
        db.create_table(u'cities_light_city', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name_ascii', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=200, blank=True)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=(), max_length=50, populate_from='name_ascii')),
            ('geoname_id', self.gf('django.db.models.fields.IntegerField')(unique=True, null=True, blank=True)),
            ('alternate_names', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.SmallIntegerField')(default=1)),
            ('default_language', self.gf('django.db.models.fields.CharField')(default='en', max_length=2)),
            ('search_names', self.gf('cities_light.models.ToSearchTextField')(default='', max_length=4000, blank=True)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cities_light.Region'], null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cities_light.Country'])),
            ('population', self.gf('django.db.models.fields.BigIntegerField')(db_index=True, null=True, blank=True)),
            ('feature_code', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=10, null=True, blank=True)),
        ))
        db.send_create_signal(u'cities_light', ['City'])

        # Adding unique constraint on 'City', fields ['region', 'slug']
        db.create_unique(u'cities_light_city', ['region_id', 'slug'])


    def backwards(self, orm):
        # Removing unique constraint on 'City', fields ['region', 'slug']
        db.delete_unique(u'cities_light_city', ['region_id', 'slug'])

        # Removing unique constraint on 'CityTranslation', fields ['language_code', 'master']
        db.delete_unique(u'cities_light_city_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'CityTranslation', fields ['name', 'language_code', 'master']
        db.delete_unique(u'cities_light_city_translation', ['name', 'language_code', 'master_id'])

        # Removing unique constraint on 'Region', fields ['country', 'slug']
        db.delete_unique(u'cities_light_region', ['country_id', 'slug'])

        # Removing unique constraint on 'RegionTranslation', fields ['language_code', 'master']
        db.delete_unique(u'cities_light_region_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'RegionTranslation', fields ['name', 'language_code', 'master']
        db.delete_unique(u'cities_light_region_translation', ['name', 'language_code', 'master_id'])

        # Removing unique constraint on 'CountryTranslation', fields ['language_code', 'master']
        db.delete_unique(u'cities_light_country_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'CountryTranslation', fields ['name', 'language_code', 'master']
        db.delete_unique(u'cities_light_country_translation', ['name', 'language_code', 'master_id'])

        # Deleting model 'CountryTranslation'
        db.delete_table(u'cities_light_country_translation')

        # Deleting model 'Country'
        db.delete_table(u'cities_light_country')

        # Deleting model 'RegionTranslation'
        db.delete_table(u'cities_light_region_translation')

        # Deleting model 'Region'
        db.delete_table(u'cities_light_region')

        # Deleting model 'CityTranslation'
        db.delete_table(u'cities_light_city_translation')

        # Deleting model 'City'
        db.delete_table(u'cities_light_city')


    models = {
        u'cities_light.city': {
            'Meta': {'unique_together': "(('region', 'slug'),)", 'object_name': 'City', 'index_together': '()'},
            'alternate_names': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.Country']"}),
            'default_language': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '2'}),
            'feature_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'geoname_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'name_ascii': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'}),
            'population': ('django.db.models.fields.BigIntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.Region']", 'null': 'True', 'blank': 'True'}),
            'search_names': ('cities_light.models.ToSearchTextField', [], {'default': "''", 'max_length': '4000', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name_ascii'"}),
            'state': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'})
        },
        u'cities_light.citytranslation': {
            'Meta': {'unique_together': "(('name', 'language_code', 'master'), ('language_code', 'master'))", 'object_name': 'CityTranslation', 'db_table': "u'cities_light_city_translation'", 'index_together': '()'},
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['cities_light.City']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'})
        },
        u'cities_light.country': {
            'Meta': {'unique_together': '()', 'object_name': 'Country', 'index_together': '()'},
            'alternate_names': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'code2': ('django.db.models.fields.CharField', [], {'max_length': '2', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'code3': ('django.db.models.fields.CharField', [], {'max_length': '3', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'continent': ('django.db.models.fields.CharField', [], {'max_length': '2', 'db_index': 'True'}),
            'default_language': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '2'}),
            'geoname_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_ascii': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name_ascii'"}),
            'state': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'tld': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '5', 'blank': 'True'})
        },
        u'cities_light.countrytranslation': {
            'Meta': {'unique_together': "(('name', 'language_code', 'master'), ('language_code', 'master'))", 'object_name': 'CountryTranslation', 'db_table': "u'cities_light_country_translation'", 'index_together': '()'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['cities_light.Country']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'cities_light.region': {
            'Meta': {'unique_together': "(('country', 'slug'),)", 'object_name': 'Region', 'index_together': '()'},
            'alternate_names': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.Country']"}),
            'default_language': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '2'}),
            'geoname_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'geoname_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_ascii': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name_ascii'"}),
            'state': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'})
        },
        u'cities_light.regiontranslation': {
            'Meta': {'unique_together': "(('name', 'language_code', 'master'), ('language_code', 'master'))", 'object_name': 'RegionTranslation', 'db_table': "u'cities_light_region_translation'", 'index_together': '()'},
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['cities_light.Region']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['cities_light']