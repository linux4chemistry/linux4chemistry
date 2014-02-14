# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LicenseModel'
        db.create_table(u'l4c_licensemodel', (
            ('label', self.gf('django.db.models.fields.CharField')(max_length=25, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'l4c', ['LicenseModel'])

        # Adding model 'Category'
        db.create_table(u'l4c_category', (
            ('label', self.gf('django.db.models.fields.CharField')(max_length=25, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'l4c', ['Category'])

        # Adding model 'Software'
        db.create_table(u'l4c_software', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('other_categories', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('license_model', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['l4c.LicenseModel'])),
            ('open_source_info', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('comments', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'l4c', ['Software'])

        # Adding M2M table for field categories on 'Software'
        m2m_table_name = db.shorten_name(u'l4c_software_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('software', models.ForeignKey(orm[u'l4c.software'], null=False)),
            ('category', models.ForeignKey(orm[u'l4c.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['software_id', 'category_id'])


    def backwards(self, orm):
        # Deleting model 'LicenseModel'
        db.delete_table(u'l4c_licensemodel')

        # Deleting model 'Category'
        db.delete_table(u'l4c_category')

        # Deleting model 'Software'
        db.delete_table(u'l4c_software')

        # Removing M2M table for field categories on 'Software'
        db.delete_table(db.shorten_name(u'l4c_software_categories'))


    models = {
        u'l4c.category': {
            'Meta': {'object_name': 'Category'},
            'label': ('django.db.models.fields.CharField', [], {'max_length': '25', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'l4c.licensemodel': {
            'Meta': {'object_name': 'LicenseModel'},
            'label': ('django.db.models.fields.CharField', [], {'max_length': '25', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'l4c.software': {
            'Meta': {'object_name': 'Software'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['l4c.Category']", 'symmetrical': 'False'}),
            'comments': ('django.db.models.fields.TextField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'license_model': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['l4c.LicenseModel']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'open_source_info': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'other_categories': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['l4c']