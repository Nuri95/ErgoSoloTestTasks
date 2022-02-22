from datetime import datetime


class CurrencyCache:
    cache_time_in_hours = 1
    data = {}
    last_update_date = None

    def _is_time_expired(self):
        if not self.last_update_date:
            return True

        return (
            datetime.now().hour - self.last_update_date.hour > self.cache_time_in_hours
        )

    def get(self, func):
        if self._is_time_expired():
            self.data = func()
            self.last_update_date = datetime.now()

        return self.data
