from abc import ABC, abstractmethod
from domain.crypto.cryptocurrency import Cryptocurrency

class CryptocurrencyRepositoryPort(ABC):

    # * Create Method
    @abstractmethod
    def get_or_create_currency(self, cryptocurrency: str):
        pass

    # * Delete Method
    @abstractmethod
    def delete_cryptocurrency(self, cryptocurrency: int):
        pass
    
    # * Update method
    @abstractmethod
    def update_all_prices(self):
        pass
