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
        
        
        
    # ? нужно ли это

    def update_all_prices(self):
        self.repository.update_all_prices()
