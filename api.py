import requests
import json
base_key = 'USD'
sym_key = 'RUB'
amount = 100


r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_key}&tsyms={sym_key}')
resp = json.loads(r.content)
new_price = resp[sym_key]*amount

print(new_price)