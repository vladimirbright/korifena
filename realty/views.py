# -*- coding: utf-8 -*-

from django.shortcuts import render


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
    c = {
        "active_link": {
            "items": "active"
        },
        "page_title": u" &mdash; Объекты"
    }
    return render(request, "index.html", c)


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

