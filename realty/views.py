# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.utils.datastructures import SortedDict

from realty.models import Offer
from realty.forms import SearchForm


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
    offers = Offer.objects.filter(**kw).select_related(
                                            "offer_type",
                                            "quarter",
                                            "apartment_type"
                                        ).order_by('-pk')
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

