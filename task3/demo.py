from currency_rates import CbCurrencyRates
from currency_rates.cache import CurrencyCache

cache = CurrencyCache()

currency_rates = CbCurrencyRates(cache)

rur_usd = currency_rates.get_currency_rate('USD')
rur_eur = currency_rates.get_currency_rate('EUR')
rur_usd2 = currency_rates.get_currency_rate('USD')
print(rur_usd, rur_eur, rur_usd2)
