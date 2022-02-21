import re
from xml.etree import ElementTree

import requests


class NoExchangeRatesError(Exception):
    pass


class CbCurrencyRates:
    def __init__(self):
        self.base_url = 'https://www.cbr.ru/scripts/XML_daily.asp'
        self.exchange_data = self._get_current_exchange_rates_data()

    def _get_current_exchange_rates_data(self):
        return requests.request('GET', self.base_url).content

    def _get_exchange_rate_against_ruble(self, to_currency):
        rate = None
        encoding = re.search(b'encoding="(.*?)"', self.exchange_data).group(1).decode()

        records = ElementTree.fromstringlist(self.exchange_data.decode(encoding))
        for record in records:
            if record.find('CharCode').text == to_currency:
                rate = record.find('Value').text.replace(',', '.')
                break

        if not rate:
            raise NoExchangeRatesError

        return float(rate)

    def get_currency_rate(self, to_currency):
        ruble_course = self._get_exchange_rate_against_ruble(to_currency)
        return round(ruble_course, 4)