from django.urls import path

from .views import (
    CryptocurrencyListView,
    CurrencyListView
)

urlpatterns = [
    path('cryptocurrencies/', CryptocurrencyListView.as_view(),
         name='cryptocurrencies'),
    path('currencies/', CurrencyListView.as_view(),
         name='currencies')
]
