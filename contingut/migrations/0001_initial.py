# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Noticia'
        db.create_table(u'contingut_noticia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titol', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('short_body', self.gf('django.db.models.fields.TextField')()),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('published_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('visits', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'contingut', ['Noticia'])

        # Adding model 'Anunci'
        db.create_table(u'contingut_anunci', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('noticia', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'anunci', to=orm['contingut.Noticia'])),
            ('titol', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('cos', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'contingut', ['Anunci'])

        # Adding model 'Sections'
        db.create_table(u'contingut_sections', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('noticia', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'section', to=orm['contingut.Noticia'])),
            ('titol', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'contingut', ['Sections'])


    def backwards(self, orm):
        # Deleting model 'Noticia'
        db.delete_table(u'contingut_noticia')

        # Deleting model 'Anunci'
        db.delete_table(u'contingut_anunci')

        # Deleting model 'Sections'
        db.delete_table(u'contingut_sections')


    models = {
        u'contingut.anunci': {
            'Meta': {'object_name': 'Anunci'},
            'cos': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'noticia': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'anunci'", 'to': u"orm['contingut.Noticia']"}),
            'titol': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'contingut.noticia': {
            'Meta': {'object_name': 'Noticia'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published_at': ('django.db.models.fields.DateTimeField', [], {}),
            'short_body': ('django.db.models.fields.TextField', [], {}),
            'titol': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'visits': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'contingut.sections': {
            'Meta': {'object_name': 'Sections'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'noticia': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'section'", 'to': u"orm['contingut.Noticia']"}),
            'titol': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        }
    }

    complete_apps = ['contingut']