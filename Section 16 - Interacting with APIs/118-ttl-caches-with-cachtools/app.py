import time
from libs.openexchange import OpenExchangeClient

APP_ID = '8e3721a8892a499389a3578a053a6e7a'

client = OpenExchangeClient(APP_ID)

usd_amount = 1000
start = time.time()
gbp_amount = OpenExchangeClient.convert(client, usd_amount, 'USD', 'GBP')
end = time.time()

print(end - start)

start = time.time()
gbp_amount = OpenExchangeClient.convert(client, usd_amount, 'USD', 'GBP')
end = time.time()

print(end - start)

start = time.time()
gbp_amount = OpenExchangeClient.convert(client, usd_amount, 'USD', 'GBP')
end = time.time()

print(end - start)

print(f'USD: {usd_amount}, GBP: {gbp_amount:.2f}')
