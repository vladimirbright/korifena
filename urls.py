# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from django.views.generic import TemplateView
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', "realty.views.index", name="index"),
    url(r'^new$', TemplateView.as_view(template_name="indexb.html")),
    (r'^admin/', include(admin.site.urls)),
)
