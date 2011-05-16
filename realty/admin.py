# -*- coding: utf-8 -*-


from django.contrib import admin


from realty.models import *


class SiteTextAdmin(admin.ModelAdmin):
    pass
admin.site.register(SiteText, SiteTextAdmin)


class SiteImageAdmin(admin.ModelAdmin):
    pass
admin.site.register(SiteImage, SiteImageAdmin)


class SiteFileAdmin(admin.ModelAdmin):
    pass
admin.site.register(SiteFile, SiteFileAdmin)


