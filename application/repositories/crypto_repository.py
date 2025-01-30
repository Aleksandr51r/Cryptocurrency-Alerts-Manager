from domain.crypto.cryptocurrency import Cryptocurrency
from infrastracture.api.api_service import CoinAPIExchangeRateProvider
from application.ports.cryptocurrency_port import CryptocurrencyRepositoryPort


class CryptocurrencyRepository(CryptocurrencyRepositoryPort):
    rate_provider = CoinAPIExchangeRateProvider()

    """

    cryptocurrency_id : btc
    currency_name : bitcoin

    """

    def __init__(self):
        self.currencies = {}
        self.currencies_in_use = {}

        self.cryptocurrency_aliases = {
            # "btc": "bitcoin",
            # "eth": "ethereum",
            # "ltc": "litecoin",
            # "xrp": "ripple",
            # "bch": "bitcoin cash"
        }

        self.cryptocurrency_aliases_long = {
            # "bitcoin": "btc",
            # "ethereum": "eth",
            # "litecoin": "ltc",
            # "ripple": "xrp",
            # "bitcoin cash": "bch"
        }

    def normalize_currency_name(self, cryptocurrency: str):
        cryptocurrency = cryptocurrency.strip().upper()
        if cryptocurrency in self.cryptocurrency_aliases_long:
            return self.cryptocurrency_aliases_long[cryptocurrency]
        elif cryptocurrency in self.cryptocurrency_aliases:
            return cryptocurrency
        return None

    def get_or_create_currency(self, user_input_cryptocurrency: str, rate_provider=rate_provider):

        new_cryptocurrency_id = self.normalize_currency_name(
            user_input_cryptocurrency)
        # print('step - normalize_currency_name', new_cryptocurrency_id)

        if new_cryptocurrency_id in self.currencies:
            # print('step -  if new_cryptocurrency_id', new_cryptocurrency_id)
            self.increment_currencies_in_use(new_cryptocurrency_id)
            # print('step -  if new_cryptocurrency_id self.currencies', self.currencies)
            # print('- step -  if new_cryptocurrency_id self.currencies_in_use',self.currencies_in_use)
            return self.currencies[new_cryptocurrency_id]
        # else:
            # print('step - else new_cryptocurrency_id', new_cryptocurrency_id)
            # print('step - else user_input_cryptocurrency',user_input_cryptocurrency)

        try:
            print('step - try fetch_name ', user_input_cryptocurrency)
            cryptocurrency_id, currency_name= rate_provider.fetch_the_name(user_input_cryptocurrency)
            currency_rate= rate_provider.get_exchange_rate(user_input_cryptocurrency)
            # print('step - currency_rate', currency_rate)
            # print('step - cryptocurrency_id currency_name',cryptocurrency_id, currency_name)
            new_currency= Cryptocurrency(
                cryptocurrency_id, currency_name.upper(), currency_rate)
            self.cryptocurrency_aliases_long[currency_name.upper(
            )] = cryptocurrency_id
            self.cryptocurrency_aliases[cryptocurrency_id] = currency_name.upper(
            )
            self.currencies_in_use[cryptocurrency_id] = 1
            self.currencies[cryptocurrency_id] = new_currency
            # print('step - after fetch new_currency', new_currency)
            # print('step - after fetch self.cryptocurrency_aliases',self.cryptocurrency_aliases)
            # print('step - after fetch self.cryptocurrency_aliases_long',self.cryptocurrency_aliases_long)
            # print('- step -  if new_cryptocurrency_id self.currencies_in_use',self.currencies_in_use)
            return new_currency
        except AttributeError as e:
            print(f"Error: {e} - AttributeError occurred")
        except ValueError as e:
            print(f"Error: {e} - ValueError occurred")
        except Exception as e:  # General exception for any other errors
            print(f"Error: {e} - Something went wrong")
            return f"Currency with name '{user_input_cryptocurrency}' wasn't found."

    def increment_currencies_in_use(self, cryptocurrency: str):
        if cryptocurrency in self.currencies_in_use:
            self.currencies_in_use[cryptocurrency] += 1

    def decrement_currencies_in_use(self, cryptocurrency: str):
        if cryptocurrency in self.currencies_in_use:
            self.currencies_in_use[cryptocurrency] -= 1
            if self.currencies_in_use[cryptocurrency] == 0:
                self.delete_cryptocurrency(cryptocurrency)

    def update_all_prices(self, target_currency: str, rate_provider=rate_provider):
        for currency in self.currencies.keys():
            try:
                # ! Fetching a price  to rest.coinapi.io
                new_price = rate_provider.get_exchange_rate(target_currency)
                # ! Set a price for each Coin
                self.currencies['currency'].update_price(
                    new_price)
                print(
                    f"Updated {currency.cryptocurrency} to {new_price} {target_currency}")
            except Exception as e:
                print(f"Failed to update {currency.cryptocurrency}: {e}")

    def delete_cryptocurrency(self, cryptocurrency: str):
        print('- step -  if new_cryptocurrency_id self.currencies_in_use',
              self.currencies_in_use)
        del self.currencies[cryptocurrency]
        del self.currencies_in_use[cryptocurrency]

    def giv_me_a_count(self):
        return self.currencies_in_use
