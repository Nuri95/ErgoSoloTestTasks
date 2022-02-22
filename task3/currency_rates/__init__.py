import re
from decimal import Decimal
from xml.etree import ElementTree

import requests

from currency_rates.const import CURRENCIES, USD, EUR


class NoExchangeRatesError(Exception):
    pass


class CbCurrencyRates:
    def __init__(self, cache):
        self.cache = cache
        self.base_url = 'https://www.cbr.ru/scripts/XML_daily.asp'

    def _get_current_exchange_rates_data(self):
        return requests.request('GET', self.base_url).content

    def get_exchange_rates_against_ruble(self):
        exchange_data = self._get_current_exchange_rates_data()

        data = {}
        encoding = re.search(b'encoding="(.*?)"', exchange_data).group(1).decode()

        records = ElementTree.fromstringlist(exchange_data.decode(encoding))
        for record in records:
            char_code = record.find('CharCode').text
            if char_code in CURRENCIES:
                rate = record.find('Value').text.replace(',', '.')
                data[char_code] = round(Decimal(rate), 2)

            if USD in data and EUR in data:
                break

        return data

    def get_currency_rates(self):
        return self.cache.get(
            self.get_exchange_rates_against_ruble
        )

