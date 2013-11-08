# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TemperatureReading'
        db.create_table('temperature_control_temperaturereading', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('temperature', self.gf('django.db.models.fields.IntegerField')()),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('temperature_control', ['TemperatureReading'])


    def backwards(self, orm):
        # Deleting model 'TemperatureReading'
        db.delete_table('temperature_control_temperaturereading')


    models = {
        'temperature_control.temperaturereading': {
            'Meta': {'object_name': 'TemperatureReading'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'temperature': ('django.db.models.fields.IntegerField', [], {}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['temperature_control']