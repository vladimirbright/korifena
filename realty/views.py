# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404

from realty.models import Offer


def index(request):
    c = {
        "active_link": {
            "index": "active"
        },
        "page_title": u""
    }
    return render(request, "index.html", c)


def services(request):
    c = {
        "active_link": {
            "services": "active"
        },
        "page_title": u" &mdash; Услуги"
    }
    return render(request, "index.html", c)


def items(request):
    offers = Offer.objects.filter(published=True)
    c = {
        "active_link": {
            "items": "active"
        },
        "page_title": u" &mdash; Объекты",
        "offers": offers
    }
    return render(request, "index.html", c)


def item_details(request, item_id, item_slug=""):
    offer = get_object_or_404(Offer, pk=item_id)
    c = {
        "active_link": {
            "items": "active"
        },
        "page_title": u" &mdash; Объекты &mdash; %s" % offer,
        "offer": offer
    }
    return render(request, "item_details.html", c)


def contacts(request):
    c = {
        "active_link": {
            "contacts": "active"
        },
        "page_title": u" &mdash; Контакты"
    }
    return render(request, "index.html", c)


def essential_elements(request):
    c = {
        "active_link": {
            "essential_elements": "active"
        },
        "page_title": u" &mdash; Реквизиты"
    }
    return render(request, "index.html", c)

