# -*- coding: utf-8 -*-


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




