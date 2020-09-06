from cachetools import cached, TTLCache
import requests


class OpenExchangeClient:
    BASE_URL = 'https://openexchangerates.org/api'

    def __init__(self, app_id):
        self.app_id = app_id

    @property
    @cached(cache=TTLCache(maxsize=2, ttl=900))  # 900 is 900 second timeout (15 minutes)
    # As long as the arguments don't change, functools will use the cached value
    def latest(self):
        return requests.get(f'{self.BASE_URL}/latest.json?app_id={self.app_id}').json()

    def convert(self, from_amount, from_currency, to_currency):
        rates = self.latest['rates']
        to_rate = rates[to_currency]

        if from_currency == 'USD':
            return from_amount * to_rate
        else:
            from_in_usd = from_amount / rates[from_currency]
            return from_in_usd * to_rate
