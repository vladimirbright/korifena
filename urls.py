# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

from realty import sitemaps as real_sitemaps

sitemaps = {
    'items': real_sitemaps.OfferSitemap,
    'services': real_sitemaps.ServiceSitemap
}

urlpatterns = patterns('',
    url(r'^$', "realty.views.index", name="index"),
    url(r'^services/$', "realty.views.services", name="services"),
    url(r'^services/(?P<item_slug>[\w_-]+)/$', "realty.views.service_details", name="service_details"),
    url(r'^items/$', "realty.views.items", name="items"),
    url(r'^items/(?P<item_id>\d+)/(?P<item_slug>[\w_-]*)$', "realty.views.item_details", name="item_details"),
    url(r'^contacts/$', "realty.views.contacts", name="contacts"),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^robots\.txt$', 'realty.views.robots'),
    (r'^admin/', include(admin.site.urls)),
)
