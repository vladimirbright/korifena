# -*- coding: utf-8 -*-


from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^korifena/', include('korifena.foo.urls')),

    (r'^admin/', include(admin.site.urls)),
)
