from datetime import datetime

from currency_rates.dto import CacheObjectInfo


class CurrencyCache:
    cache_time_in_hours = 1
    data = {}

    def _is_time_expired(self, currency):
        cache_info = self.data.get(currency)
        if not cache_info:
            return True

        return (
            datetime.now().hour - cache_info.date.hour > self.cache_time_in_hours
        )

    def get_currency_rate(self, func, currency):
        if self._is_time_expired(currency):
            rate = func(currency)
            self.data[currency] = CacheObjectInfo(rate, datetime.now())

        return self.data[currency].rate
