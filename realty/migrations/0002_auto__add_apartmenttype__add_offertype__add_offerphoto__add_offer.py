# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ApartmentType'
        db.create_table('realty_apartmenttype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('sort', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, db_index=True)),
        ))
        db.send_create_signal('realty', ['ApartmentType'])

        # Adding model 'OfferType'
        db.create_table('realty_offertype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('sort', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, db_index=True)),
        ))
        db.send_create_signal('realty', ['OfferType'])

        # Adding model 'OfferPhoto'
        db.create_table('realty_offerphoto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('offer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['realty.Offer'])),
            ('img', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('realty', ['OfferPhoto'])

        # Adding model 'Offer'
        db.create_table('realty_offer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('offer_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['realty.OfferType'])),
            ('appartment_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['realty.ApartmentType'])),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('holded', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('realty', ['Offer'])


    def backwards(self, orm):
        
        # Deleting model 'ApartmentType'
        db.delete_table('realty_apartmenttype')

        # Deleting model 'OfferType'
        db.delete_table('realty_offertype')

        # Deleting model 'OfferPhoto'
        db.delete_table('realty_offerphoto')

        # Deleting model 'Offer'
        db.delete_table('realty_offer')


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
