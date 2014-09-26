# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Article.publication_date'
        db.add_column(u'blog_article', 'publication_date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 1, 1, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Article.publication_date'
        db.delete_column(u'blog_article', 'publication_date')


    models = {
        u'blog.article': {
            'Meta': {'object_name': 'Article'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Category']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publication_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 1, 1, 0, 0)'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '240'})
        },
        u'blog.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        }
    }

    complete_apps = ['blog']