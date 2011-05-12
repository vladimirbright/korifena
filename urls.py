# -*- coding: utf-8 -*-


from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', "realty.views.index", name="index"),

    (r'^admin/', include(admin.site.urls)),
)
