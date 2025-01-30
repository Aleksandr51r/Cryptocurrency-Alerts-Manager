from domain.crypto.cryptocurrency_ABC import Cryptocurrency_ABC


class Cryptocurrency(Cryptocurrency_ABC):
    def __init__(self, cryptocurrency_id: str, currency_name: str, currency_rate: float):
        self.cryptocurrency_id = cryptocurrency_id
        self.currency_name = currency_name
        self.currency_rate = currency_rate

    def update_price(self, new_price: float):
        self.currency_rate = new_price

    def __str__(self):
        return f"{self.cryptocurrency_id}'s rate : {self.currency_rate}"
