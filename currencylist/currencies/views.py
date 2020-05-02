from django.shortcuts import render
from django.views.generic import ListView

from .models import Cryptocurrency, Currency


class CryptocurrencyListView(ListView):
    """ Cryptocurrency list view """
    model = Cryptocurrency
    template_name = 'currencies/cryptocurrencies.html'
    context_object_name = 'cryptocurrencies'


class CurrencyListView(ListView):
    """ Currency list view """
    model = Currency
    template_name = 'currencies/currencies.html'
    context_object_name = 'currencies'
