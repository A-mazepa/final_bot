#функционал, связанный с конвертацией
import requests
import json
from config import exchanges

class ApiExeption(Exception):
    pass

class Converter:
    @staticmethod
    def get_price(base, sym, amount):
        try:
            base_key = exchanges[base.lower()]
        except KeyError:
            return ApiExeption(f"Валюта {base} не найдена")

        try:
            sym_key = exchanges[sym.lower()]
        except KeyError:
            return ApiExeption(f'Валюта {sym} не найдена')

        if base_key == sym_key:
            raise ApiExeption(f'Невозможно перевести одинаковые валюты {base}')

        try:
            amount = float(amount.replace(',', '.'))
        except ValueError:
            raise ApiExeption(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_key}&tsyms={sym_key}')
        resp = json.loads(r.content)
        new_price = resp[sym_key] * float(amount)
        return round(new_price, 2)
