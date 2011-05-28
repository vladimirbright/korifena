# -*- coding: utf-8 -*-

from django.contrib.sitemaps import Sitemap

from realty.models import Offer, Service

class OfferSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Offer.objects.filter(published=True, holded=False)

    def lastmod(self, obj):
        return obj.added


class ServiceSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Service.objects.filter(published=True)

