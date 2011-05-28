# -*- coding: utf-8 -*-

import pytils

from django.db import models


class SiteText(models.Model):
    slug = models.SlugField(u"Короткое название")
    body = models.TextField(u"Текст")

    def __unicode__(self):
        return u"Text: %s" % self.slug

    class Meta:
        verbose_name = u"Текст"
        verbose_name_plural = u"Тексты"


class SiteImage(models.Model):
    slug = models.SlugField(u"Короткое название")
    file = models.ImageField(u"Картинка", upload_to="uploads/img")

    def __unicode__(self):
        return u"Img: %s" % self.slug

    class Meta:
        verbose_name = u"Картинка"
        verbose_name_plural = u"Картинки"


class SiteFile(models.Model):
    slug = models.SlugField(u"Короткое название")
    file = models.ImageField(u"Файл", upload_to="uploads/file")

    def __unicode__(self):
        return u"File: %s" % self.slug

    class Meta:
        verbose_name = u"Файл"
        verbose_name_plural = u"Файлы"

SORT_HELP_TEXT = u"Меньше, значит выше"

class OfferType(models.Model):
    title = models.CharField(u"Название", max_length=100)
    sort = models.PositiveIntegerField(u"Сортировка", default=0, db_index=True, help_text=SORT_HELP_TEXT)

    def __unicode__(self):
        return u"%s" % self.title

    class Meta:
        verbose_name = u"Тип предложения"
        verbose_name_plural = u"Тип предложения"
        ordering = [ "sort" ]


class ApartmentType(models.Model):
    title = models.CharField(u"Название", max_length=100)
    sort = models.PositiveIntegerField(u"Сортировка", default=0, db_index=True, help_text=SORT_HELP_TEXT)

    def __unicode__(self):
        return u"%s" % self.title

    class Meta:
        verbose_name = u"Тип объекта"
        verbose_name_plural = u"Тип объекта"
        ordering = [ "sort" ]


class Quarter(models.Model):
    title = models.CharField(u"Название", max_length=100)
    sort = models.PositiveIntegerField(u"Сортировка", default=0, db_index=True, help_text=SORT_HELP_TEXT)

    def __unicode__(self):
        return u"%s" % self.title

    class Meta:
        verbose_name = u"Район города"
        verbose_name_plural = u"Районы города"
        ordering = [ "sort" ]


class Offer(models.Model):
    offer_type = models.ForeignKey(OfferType, verbose_name=u"Аренда/Продажа")
    apartment_type = models.ForeignKey(ApartmentType, verbose_name=u"Тип объекта")
    quarter = models.ForeignKey(Quarter, verbose_name=u"Район города")
    text = models.TextField(u"Объявление")
    added = models.DateTimeField(u"Добавлено", auto_now_add=True, editable=True)
    holded = models.BooleanField(u"Сдана/Продана", default=False)
    published = models.BooleanField(u"Публиковать", default=True)
    slug = models.SlugField(max_length=200, editable=False)

    def __unicode__(self):
        return u"Объявление: [%s] %s %s %s" %(
            self.offer_type,
            self.quarter,
            self.apartment_type,
            self.text[:50].replace("\n","").replace("\r", "").replace("\t", "")
        )

    @models.permalink
    def get_absolute_url(self):
        return ( "realty.views.item_details", [ self.pk, self.slug ])

    def save(self, *args, **kwargs):
        s = u"%s %s %s" %(
            self.offer_type.title,
            self.apartment_type.title,
            self.quarter.title
        )
        self.slug = pytils.translit.slugify(s)[:200]
        return super(Offer, self).save(*args, **kwargs)

    class Meta:
        verbose_name = u"Объект"
        verbose_name_plural = u"Объекты"
        ordering = [ "-added" ]


class OfferPhoto(models.Model):
    offer = models.ForeignKey(Offer)
    img = models.ImageField(u"Картинка", upload_to="uploads/offers")

    def __unicode__(self):
        return u"Фотография"

    class Meta:
        verbose_name = u"Фото"
        verbose_name_plural = u"Фото"


class Service(models.Model):
    title = models.CharField(u"Название", max_length=200)
    description = models.TextField(u"Описание")
    slug = models.SlugField(u"Кусок ссылки", max_length=200)
    sort = models.PositiveIntegerField(u"Сортировка", default=0, db_index=True, help_text=SORT_HELP_TEXT)
    published = models.BooleanField(u"Публиковать", default=True)

    def __unicode__(self):
        return u"Услуга: %s" % self.title[:70]

    @models.permalink
    def get_absolute_url(self):
        return ("service_details", [ self.slug, ])

    class Meta:
        verbose_name = u"Услуга"
        verbose_name_plural = u"Услуги"
        ordering = [ "sort" ]

