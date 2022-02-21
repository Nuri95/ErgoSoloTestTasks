from currency_rates import CbCurrencyRates

currency_rates = CbCurrencyRates()
rur_usd = currency_rates.get_currency_rate('USD')
rur_eur = currency_rates.get_currency_rate('EUR')
print(rur_eur, rur_eur)