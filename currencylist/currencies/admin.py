from django.contrib import admin

from .models import Cryptocurrency, Currency


@admin.register(Cryptocurrency)
class CryptocurrencyModelAdmin(admin.ModelAdmin):
    """ Cryptocurrency model admin """
    list_display = ('abbreviation', 'name', 'price', 'change')


@admin.register(Currency)
class CurrencyModelAdmin(admin.ModelAdmin):
    """ Currency model admin """
    list_display = ('abbreviation', 'name', 'price', 'unit')
