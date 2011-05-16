# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', "realty.views.index", name="index"),
    url(r'^services$', "realty.views.services", name="services"),
    url(r'^items$', "realty.views.items", name="items"),
    url(r'^contacts$', "realty.views.contacts", name="contacts"),
    url(r'^essential-elements$', "realty.views.essential_elements", name="essential_elements"),
    (r'^admin/', include(admin.site.urls)),
)
