import requests
import json
from config import keys
class ApiException(Exception):
    pass
                    #Отлов ошибок
class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ApiException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ApiException(f'Не удалость обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ApiException(f'Не удалость обработать валюту {quote}')

        try:
            amount = float(amount)
        except ValueError:
            raise ApiException(f'Не удалость обработать колличество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base * amount
                    #Отлов ошибок