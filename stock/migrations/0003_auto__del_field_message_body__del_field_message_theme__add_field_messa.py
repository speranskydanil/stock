# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Message.body'
        db.delete_column(u'stock_message', 'body')

        # Deleting field 'Message.theme'
        db.delete_column(u'stock_message', 'theme')

        # Adding field 'Message.subject'
        db.add_column(u'stock_message', 'subject',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=120),
                      keep_default=False)

        # Adding field 'Message.message'
        db.add_column(u'stock_message', 'message',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Message.body'
        db.add_column(u'stock_message', 'body',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'Message.theme'
        db.add_column(u'stock_message', 'theme',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=120),
                      keep_default=False)

        # Deleting field 'Message.subject'
        db.delete_column(u'stock_message', 'subject')

        # Deleting field 'Message.message'
        db.delete_column(u'stock_message', 'message')


    models = {
        u'stock.message': {
            'Meta': {'object_name': 'Message'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        }
    }

    complete_apps = ['stock']