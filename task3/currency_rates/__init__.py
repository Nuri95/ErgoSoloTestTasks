import re
from xml.etree import ElementTree

import requests


class NoExchangeRatesError(Exception):
    pass


class CbCurrencyRates:
    def __init__(self, cache):
        self.cache = cache
        self.base_url = 'https://www.cbr.ru/scripts/XML_daily.asp'

    def _get_current_exchange_rates_data(self):
        return requests.request('GET', self.base_url).content

    def get_exchange_rate_against_ruble(self, to_currency):
        exchange_data = self._get_current_exchange_rates_data()

        rate = None
        encoding = re.search(b'encoding="(.*?)"', exchange_data).group(1).decode()

        records = ElementTree.fromstringlist(exchange_data.decode(encoding))
        for record in records:
            if record.find('CharCode').text == to_currency:
                rate = record.find('Value').text.replace(',', '.')
                break

        if not rate:
            raise NoExchangeRatesError

        return round(float(rate), 4)

    def get_currency_rate(self, to_currency):
        return self.cache.get_currency_rate(
            self.get_exchange_rate_against_ruble,
            to_currency
        )

