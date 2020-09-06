import requests

APP_ID = '8e3721a8892a499389a3578a053a6e7a'
ENDPOINT = 'https://openexchangerates.org/api/latest.json'

response = requests.get(f'{ENDPOINT}?app_id={APP_ID}')
exchange_rates = response.json()['rates']
