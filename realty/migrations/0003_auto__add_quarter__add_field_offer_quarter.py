# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Quarter'
        db.create_table('realty_quarter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('sort', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, db_index=True)),
        ))
        db.send_create_signal('realty', ['Quarter'])

        # Adding field 'Offer.quarter'
        db.add_column('realty_offer', 'quarter', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['realty.Quarter']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'Quarter'
        db.delete_table('realty_quarter')

        # Deleting field 'Offer.quarter'
        db.delete_column('realty_offer', 'quarter_id')


    models = {
        'realty.apartmenttype': {
            'Meta': {'ordering': "['sort']", 'object_name': 'ApartmentType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sort': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'realty.offer': {
            'Meta': {'ordering': "['added']", 'object_name': 'Offer'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'appartment_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['realty.ApartmentType']"}),
            'holded': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'offer_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['realty.OfferType']"}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'quarter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['realty.Quarter']"}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'realty.offerphoto': {
            'Meta': {'object_name': 'OfferPhoto'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'offer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['realty.Offer']"})
        },
        'realty.offertype': {
            'Meta': {'ordering': "['sort']", 'object_name': 'OfferType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sort': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'realty.quarter': {
            'Meta': {'ordering': "['sort']", 'object_name': 'Quarter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sort': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'realty.sitefile': {
            'Meta': {'object_name': 'SiteFile'},
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'realty.siteimage': {
            'Meta': {'object_name': 'SiteImage'},
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'realty.sitetext': {
            'Meta': {'object_name': 'SiteText'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['realty']
