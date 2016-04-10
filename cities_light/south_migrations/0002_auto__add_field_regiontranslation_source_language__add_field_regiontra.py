# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'RegionTranslation.source_language'
        db.add_column(u'cities_light_region_translation', 'source_language',
                      self.gf('django.db.models.fields.CharField')(default='en', max_length=2),
                      keep_default=False)

        # Adding field 'RegionTranslation.is_auto_translated'
        db.add_column(u'cities_light_region_translation', 'is_auto_translated',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Country.allow_translate'
        db.add_column(u'cities_light_country', 'allow_translate',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'City.allow_translate'
        db.add_column(u'cities_light_city', 'allow_translate',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Region.allow_translate'
        db.add_column(u'cities_light_region', 'allow_translate',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'CityTranslation.source_language'
        db.add_column(u'cities_light_city_translation', 'source_language',
                      self.gf('django.db.models.fields.CharField')(default='en', max_length=2),
                      keep_default=False)

        # Adding field 'CityTranslation.is_auto_translated'
        db.add_column(u'cities_light_city_translation', 'is_auto_translated',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'CountryTranslation.source_language'
        db.add_column(u'cities_light_country_translation', 'source_language',
                      self.gf('django.db.models.fields.CharField')(default='en', max_length=2),
                      keep_default=False)

        # Adding field 'CountryTranslation.is_auto_translated'
        db.add_column(u'cities_light_country_translation', 'is_auto_translated',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'RegionTranslation.source_language'
        db.delete_column(u'cities_light_region_translation', 'source_language')

        # Deleting field 'RegionTranslation.is_auto_translated'
        db.delete_column(u'cities_light_region_translation', 'is_auto_translated')

        # Deleting field 'Country.allow_translate'
        db.delete_column(u'cities_light_country', 'allow_translate')

        # Deleting field 'City.allow_translate'
        db.delete_column(u'cities_light_city', 'allow_translate')

        # Deleting field 'Region.allow_translate'
        db.delete_column(u'cities_light_region', 'allow_translate')

        # Deleting field 'CityTranslation.source_language'
        db.delete_column(u'cities_light_city_translation', 'source_language')

        # Deleting field 'CityTranslation.is_auto_translated'
        db.delete_column(u'cities_light_city_translation', 'is_auto_translated')

        # Deleting field 'CountryTranslation.source_language'
        db.delete_column(u'cities_light_country_translation', 'source_language')

        # Deleting field 'CountryTranslation.is_auto_translated'
        db.delete_column(u'cities_light_country_translation', 'is_auto_translated')


    models = {
        u'cities_light.city': {
            'Meta': {'unique_together': "(('region', 'slug'),)", 'object_name': 'City', 'index_together': '()'},
            'allow_translate': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
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
            'is_auto_translated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['cities_light.City']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'source_language': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '2'})
        },
        u'cities_light.country': {
            'Meta': {'unique_together': '()', 'object_name': 'Country', 'index_together': '()'},
            'allow_translate': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
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
            'is_auto_translated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['cities_light.Country']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'source_language': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '2'})
        },
        u'cities_light.region': {
            'Meta': {'unique_together': "(('country', 'slug'),)", 'object_name': 'Region', 'index_together': '()'},
            'allow_translate': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
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
            'is_auto_translated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['cities_light.Region']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'source_language': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '2'})
        }
    }

    complete_apps = ['cities_light']