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


class OfferTypeAdmin(admin.ModelAdmin):
    list_display = [ "title", "sort" ]
    list_editable = [ "sort", ]
admin.site.register(OfferType, OfferTypeAdmin)


class ApartmentTypeAdmin(admin.ModelAdmin):
    list_display = [ "title", "sort" ]
    list_editable = [ "sort", ]
admin.site.register(ApartmentType, ApartmentTypeAdmin)


class QuarterAdmin(admin.ModelAdmin):
    list_display = [ "title", "sort" ]
    list_editable = [ "sort", ]
admin.site.register(Quarter, QuarterAdmin)


class OfferPhotoAdmin(admin.ModelAdmin):
    pass
admin.site.register(OfferPhoto, OfferPhotoAdmin)


class OfferImageAdminInline(admin.TabularInline):
    extra = 0
    can_delete = True
    model = OfferPhoto


class OfferAdmin(admin.ModelAdmin):
    def offer_title(self, obj):
        return u"%s %s %s %s" %(
            obj.offer_type,
            obj.apartment_type,
            obj.quarter,
            obj.text[:100]
        )

    list_display = (
        "offer_title",
        "holded",
        "published",
        "added"
    )
    list_filter = (
        "offer_type",
        "apartment_type",
        "quarter",
        "added"
    )
    readonly_fields = ( "slug", )
    inlines = ( OfferImageAdminInline, )
admin.site.register(Offer, OfferAdmin)
