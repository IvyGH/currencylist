import requests
import lxml
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand
from currencies.models import Cryptocurrency, Currency


class Command(BaseCommand):
    help = 'Collect currencies'

    def __init__(self):
        self.HEADERS = {
            'accept': '*/*',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'
        }
        self.session = requests.Session()

    def parse_cryptocurrencies(self):
        URL = 'https://myfin.by/crypto-rates'
        response = self.session.get(URL, headers=self.HEADERS)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')
        abbreviations = soup.find_all('div',
                                      attrs={'class': 'crypto_iname hidden-xs'})
        names = soup.find_all('a', attrs={'class': 's-bold'})
        prices = soup.find_all('div', attrs={'class': 'fs-12'})
        changes = soup.find_all('div', attrs={'class': ['fs-12 down', 'fs-12 stable', 'fs-12 up']})
        for abbreviation, name, price, change in zip(abbreviations, names, prices, changes):
            try:
                Cryptocurrency.objects.update_or_create(
                    abbreviation=abbreviation.text,
                    name=name.text,
                    price=price.previous.replace('$ ', ''),
                    change=change.text
                )
                print(f'{name.text} cryptocurrency updated or added.')
            except:
                pass

    def parse_currencies(self):
        URL = 'https://myfin.by/bank/kursy_valjut_nbrb'
        response = self.session.get(URL, headers=self.HEADERS)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')
        abbreviations = soup.find_all('span', attrs={'class': 'flag'})
        names = soup.find_all('a', attrs={'data-pjax': '0'})
        prices = soup.find_all('a', attrs={'data-pjax': '0'})
        units = soup.find_all('span', attrs={'class': 'flag'})
        for abbreviation, name, price, unit in zip(abbreviations, names, prices, units):
            try:
                Currency.objects.update_or_create(
                    abbreviation=abbreviation.next,
                    name=name.text,
                    price=price.next.next.text,
                    unit=unit.next.next.text
                )
                print(f'{name.text} currency updated or added.')
            except:
                pass

    def handle(self, *args, **options):
        self.parse_cryptocurrencies()
        self.parse_currencies()
