# -*- coding: utf-8 -*-

from django import forms

from realty.models import OfferType, Quarter, ApartmentType


class SearchForm(forms.Form):
    offer_type = forms.ModelChoiceField(
                     queryset=OfferType.objects.all(),
                     required=False,
                     empty_label=u"Не важно",
                     widget=forms.RadioSelect
                 )
    quarter = forms.ModelChoiceField(
                  queryset=Quarter.objects.all(),
                  required=False,
                  empty_label=u"Не важно",
                  widget=forms.RadioSelect
              )
    apartment_type = forms.ModelChoiceField(
                         queryset=ApartmentType.objects.all(),
                         required=False,
                         empty_label=u"Не важно",
                         widget=forms.RadioSelect
                     )

