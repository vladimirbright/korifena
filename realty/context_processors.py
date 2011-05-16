# -*- coding: utf-8 -*-

from realty.models import SiteText


def get_site_data(request):
    u"""
        Достаем всю инфу нужную на всех страницах.
    """
    phone, c = SiteText.objects.get_or_create(slug="phone_number")
    if c:
        phone.body = u"8 (928) 5 555 555"
        phone.save()
    email, c = SiteText.objects.get_or_create(slug="email")
    if c:
        email.body = u"evgenia@korifena.ru"
        email.save()
    title, c = SiteText.objects.get_or_create(slug="company_title")
    if c:
        title.body = u"&laquo;Корифена&raquo;"
        title.save()
    return {
        "on_site_contacs": {
            "phone": phone.body,
            "email": email.body,
            "buisness_title": title.body,
        }
    }




