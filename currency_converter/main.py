import requests
import json
from typing import Final

BASE_URL: str = '' ## If we want to use real data, call API with URL
API_KEY: str = '' ## If the API need an API key

def get_rates(isMock: bool = True) -> dict:
    if isMock:
        with open('currency_rates.json', 'r') as file:
            return json.load(file)
    payload: dict = {'access_key': API_KEY}
    request = requests.get(BASE_URL, params=payload)
    data: dict = request.json()

    with open('currency_rates.json', 'w') as file:
            json.dump(data, file)

    return data

def get_currency_amount(currency: str, rates: dict) -> float:
     currency: str = currency.upper()
     if currency in rates.keys():
          return rates.get(currency)
     else:
          raise ValueError(f'{currency} is not a valid currency.')


def convert_currency(amount: float, base: str, vs: str, rates: dict) -> float:
     base_currency_amount: float = get_currency_amount(base, rates)
     vs_currency_amount: float = get_currency_amount(vs, rates)

     conversion: float = round((vs_currency_amount / base_currency_amount) * amount, 2)
     print(f'{amount:,.2f} ({base}) is {conversion:,.2f} ({vs})')
     return conversion

def main():
     data: dict = get_rates(isMock=True)
     rates: dict = data.get('rates')

     convert_currency(1000000, 'IDR', 'JPY', rates=rates)

if __name__ == "__main__":
     main()