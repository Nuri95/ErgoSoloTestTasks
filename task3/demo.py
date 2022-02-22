from currency_rates import CbCurrencyRates
from currency_rates.cache import CurrencyCache

cache = CurrencyCache()

currency_rates = CbCurrencyRates(cache)

rates = currency_rates.get_currency_rates()
print(rates)

