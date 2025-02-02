from application.ports.cryptocurrency_port import CryptocurrencyRepositoryPort
from domain.crypto.cryptocurrency import Cryptocurrency


class CryptocurrencyAdapter:
    def __init__(self, repository: CryptocurrencyRepositoryPort):
        self.repository = repository

    def create_currency(self, cryptocurrency: str):
        cryptocurrency = Cryptocurrency(cryptocurrency)
        self.repository.get_or_create_currency(cryptocurrency)

    def delete_cryptocurrency(self, cryptocurrency: str):
        self.repository.delete_cryptocurrency(cryptocurrency)

    def get_crypto_alerts_count(self):
        return self.repository.get_currencies_in_use()

    def get_cryptocurrency(self, cryptocurrency: str):
        return self.repository.get_or_create_currency(cryptocurrency)

    # ? нужно ли это

    def update_all_prices(self):
        self.repository.update_all_prices()

    def manage_list_cryptocurrency_incresment(self, cryptocurrency: str):
        return self.repository.increment_currencies_in_use(cryptocurrency)

    def manage_list_cryptocurrency_decrement(self, cryptocurrency: str):
        return self.repository.decrement_currencies_in_use(cryptocurrency)

# * Read Methods
# * Delete Method
# * Create Method
