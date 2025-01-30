from abc import ABC, abstractmethod

class Cryptocurrency_ABC(ABC):
    
    @abstractmethod
    def update_price(self, new_price: float):
        pass

