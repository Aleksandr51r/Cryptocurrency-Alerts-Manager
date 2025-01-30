from abc import ABC, abstractmethod

class ExchangeRateProvider(ABC):
    
    @abstractmethod
    def get_exchange_rate(self, base_currency: str) -> float:
        pass