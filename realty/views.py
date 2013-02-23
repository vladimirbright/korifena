# -*- coding: utf-8 -*-

from django.contrib.sites.models import Site
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils.datastructures import SortedDict

from realty.models import Offer, Service, SiteText, SiteImage
from realty.forms import SearchForm


def index(request):
    try:
        self_photo = SiteImage.objects.get(slug="self_photo")
    except SiteImage.DoesNotExist:
        self_photo = None
    first_paragraph, cr = SiteText.objects.get_or_create(slug="index_first_paragraph")
    if cr:
        first_paragraph.body = u"""
        Раздел находится в процессе наполнения
"""
        first_paragraph.save()
    second_paragraph, cr = SiteText.objects.get_or_create(slug="index_second_paragraph")
    c = {
        "active_link": {
            "index": "active"
        },
        "page_title": u"",
        "last_offers": Offer.objects.filter(published=True).select_related("offer_type", "quarter", "apartment_type")[:5],
        "services": Service.objects.filter(published=True)[:5],
        "self_photo": self_photo,
        "first_paragraph": first_paragraph,
        "second_paragraph": second_paragraph,
    }
    return render(request, "index_page.html", c)


def services(request):
    service_text, cre = SiteText.objects.get_or_create(slug="service_text")
    if cre:
        service_text.body = u"""
Агентство недвижимости оказывают услуги для физических и юридических лиц, занимаясь подбором объектов недвижимости (квартир, домов, складов) и оформлением сделок купли-продажи. В настоящее время достаточно сложно найти для съема или покупки подходящую квартиру. Агентство недвижимости обладает большой базой данных объектов, сдающихся в аренду или выставленных на продажу. Обратившись в нашу компанию, вы экономите большое количество своего времени.
Для юридических лиц, которым необходимы офисные, торговые, складские и производственные помещения, агентство недвижимости также окажет неоценимую помощь. Опытные и знающие свое дело специалисты агентства недвижимости помогут вам подобрать именно ту недвижимость, которая устроит вас по всем параметрам.

Кроме подбора объектов недвижимости и оформления сделок по купле-продаже, мы также можем произвести оценку недвижимости, проверить правильность оформления права собственности и готовность все документов, необходимых для проведения сделки.

*Оплата услуг агентства недвижимости производится по факту завершения действия заключенного агентского договора.*
"""
        service_text.save()
    c = {
        "active_link": {
            "services": "active"
        },
        "page_title": u" &mdash; Услуги",
        "last_offers": Offer.objects.filter(published=True).select_related("offer_type", "quarter", "apartment_type")[:5],
        "services": Service.objects.filter(published=True)[:5],
        "all_services": Service.objects.filter(published=True),
        "service_text": service_text,
    }
    return render(request, "services.html", c)


def service_details(request, item_slug):
    service = get_object_or_404(Service, slug=item_slug, published=True)
    c = {
        "active_link": {
            "services": "active"
        },
        "page_title": u" &mdash; Услуги &mdash; %s" % service.title,
        "last_offers": Offer.objects.filter(published=True).select_related("offer_type", "quarter", "apartment_type")[:5],
        "services": Service.objects.filter(published=True)[:5],
        "service": service
    }
    return render(request, "service_details.html", c)


def items(request):
    form = SearchForm(request.GET or None)
    offer_type = None
    quarter = None
    apartment_type = None
    kw = SortedDict()
    kw["published"] = True
    if form.is_valid():
        offer_type = form.cleaned_data.get("offer_type", None)
        if offer_type:
            kw["offer_type"] = offer_type
        quarter = form.cleaned_data.get("quarter", None)
        if quarter:
            kw["quarter"] = quarter
        apartment_type = form.cleaned_data.get("apartment_type", None)
        if apartment_type:
            kw["apartment_type"] = apartment_type
    offers = Offer.objects.filter(**kw).select_related("offer_type", "quarter", "apartment_type")
    c = {
        "active_link": {
            "items": "active"
        },
        "page_title": u" &mdash; Объекты",
        "offers": offers,
        "search_form": form,
        "offer_type": offer_type,
        "quarter": quarter,
        "apartment_type": apartment_type,
    }
    return render(request, "items.html", c)


def item_details(request, item_id, item_slug=""):
    offer = get_object_or_404(Offer, pk=item_id)
    c = {
        "active_link": {
            "items": "active"
        },
        "page_title": u" &mdash; Объекты &mdash; %s" % offer,
        "offer": offer,
        "other_offers": Offer.objects.filter(published=True, quarter=offer.quarter).exclude(pk=offer.pk)
    }
    return render(request, "item_details.html", c)


def contacts(request):
    contacts_text , cre = SiteText.objects.get_or_create(slug="contacs_text")
    if cre:
        contacts_text.body = u"""
h2. Контакты

Тут должны быть контакты.


h2. Реквизиты

Тут должны быть реквизиты

*Мы клевые*
"""
        contacts_text.save()
    c = {
        "active_link": {
            "contacts": "active"
        },
        "page_title": u" &mdash; Контакты",
        "last_offers": Offer.objects.filter(published=True).select_related("offer_type", "quarter", "apartment_type")[:5],
        "services": Service.objects.filter(published=True)[:5],
        "contacts_text": contacts_text
    }
    return render(request, "contacs.html", c)


def robots(request):
    robots_text , cre = SiteText.objects.get_or_create(slug="robots.txt")
    cur_site = Site.objects.get_current()
    if cre:
        robots_text.body = u"""
User-agent: Yandex
Allow: /
Sitemap: http://%(domain)s/sitemap.xml
Disallow: /admin/

User-agent: Google
Allow: /
Sitemap: http://%(domain)s/sitemap.xml
Disallow: /admin/

User-agent: Rambler
Allow: /
Sitemap: http://%(domain)s/sitemap.xml
Disallow: /admin/

User-agent: Yahoo
Allow: /
Sitemap: http://%(domain)s/sitemap.xml
Disallow: /admin/

User-agent: Nigma
Allow: /
Sitemap: http://%(domain)s/sitemap.xml
Disallow: /admin/

User-agent: *
Allow: /
Sitemap: http://%(domain)s/sitemap.xml
Disallow: /admin/
""" % { "domain": cur_site.domain }
        robots_text.body = robots_text.body.strip()
        robots_text.save()
    response = HttpResponse(robots_text.body)
    response["content-type"] = "text/plain"
    return response
