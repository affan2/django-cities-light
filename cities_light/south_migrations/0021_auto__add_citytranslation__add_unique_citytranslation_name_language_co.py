# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration, DataMigration
from django.db import models
from django.db import connection



class Migration(SchemaMigration, DataMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'City', fields ['region', 'name']
        db.delete_unique(u'cities_light_city', ['region_id', 'name'])

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

        index = 0
        cursor = connection.cursor()
        count = cursor.execute("SELECT id, name, display_name FROM cities_light_city")
        while index<count:
            index+=1
            obj = orm['cities_light.citytranslation']()
            row = cursor.fetchone()
            obj.name = row[1]
            obj.display_name = row[2]
            obj.master = orm['cities_light.city'].objects.get(id=row[0])
            obj.language_code = 'en'
            try:
                obj.save()
                print ">citytranslation>>>>>",obj.name
            except :
                pass

        # # Deleting field 'City.display_name'
        # db.delete_column(u'cities_light_city', 'display_name')
        #
        # # Deleting field 'City.name'
        # db.delete_column(u'cities_light_city', 'name')


    def backwards(self, orm):
        # Removing unique constraint on 'CityTranslation', fields ['name', 'language_code', 'master']
        db.delete_unique(u'cities_light_city_translation', ['name', 'language_code', 'master_id'])

        # Deleting model 'CityTranslation'
        db.delete_table(u'cities_light_city_translation')

        # # Adding field 'City.display_name'
        # db.add_column(u'cities_light_city', 'display_name',
        #               self.gf('django.db.models.fields.CharField')(default='', max_length=200),
        #               keep_default=False)
        #
        # # Adding field 'City.name'
        # db.add_column(u'cities_light_city', 'name',
        #               self.gf('django.db.models.fields.CharField')(default='', max_length=200, db_index=True),
        #               keep_default=False)

        # Adding unique constraint on 'City', fields ['region', 'name']
        db.create_unique(u'cities_light_city', ['region_id', 'name'])


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
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name_ascii'"})
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
            'tld': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '5', 'blank': 'True'})
        },
        u'cities_light.countrytranslation': {
            'Meta': {'unique_together': "(('name', 'language_code', 'master'), ('language_code', 'master'))", 'object_name': 'CountryTranslation', 'db_table': "u'cities_light_country_translation'", 'index_together': '()'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['cities_light.Country']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
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
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name_ascii'"})
        },
        u'cities_light.regiontranslation': {
            'Meta': {'unique_together': "(('name', 'language_code', 'master'), ('language_code', 'master'))", 'object_name': 'RegionTranslation', 'db_table': "u'cities_light_region_translation'", 'index_together': '()'},
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['cities_light.Region']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        }
    }

    complete_apps = ['cities_light']
