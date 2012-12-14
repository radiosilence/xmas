# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Card.viewed'
        db.add_column(u'xmas_card', 'viewed',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Card.viewed'
        db.delete_column(u'xmas_card', 'viewed')


    models = {
        u'xmas.card': {
            'Meta': {'object_name': 'Card'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'recipient': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'viewed': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['xmas']