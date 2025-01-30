import requests
# from infrastracture.api.api_port import ExchangeRateProvider
import json


class CoinAPIExchangeRateProvider():

    def __init__(self):

        self.API_KEY_VALUE = '5cba0eef-fd97-470f-99be-bb5757f150f0'
        self.one_asset_url = "https://rest.coinapi.io/v1/exchangerate"
        self.assets_url = "https://rest.coinapi.io/v1/assets"
        self.headers = {
            'Accept': 'application/json',
            'X-CoinAPI-Key': self.API_KEY_VALUE
        }

    def get_exchange_rate(self, asset_id_base: str):
        url = f"{self.one_asset_url}/{asset_id_base}/USD"

        print(f'Searching for excange rate for {asset_id_base}')
        print('...')
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            print('Suscess !')
            data = response.json()
            return data['rate']
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")

    def fetch_the_name(self, asset_id_base):
        url = f"{self.assets_url}/{asset_id_base}"
        print(
            f'Searching for to find a cryptocurrency whith a name {asset_id_base}')

        print('...')
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            print('Suscess !')
            data = response.json()
            return data[0]['asset_id'], data[0]['name']
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")


# api_provider = CoinAPIExchangeRateProvider()

# BTC_data = api_provider.fetch_the_name('BTC')
# print(BTC_data)
# BTC_data = api_provider.get_exchange_rate('BTC')
# print(BTC_data)
