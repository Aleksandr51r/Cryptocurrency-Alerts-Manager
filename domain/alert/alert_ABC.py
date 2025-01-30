from abc import ABC, abstractmethod
from domain.crypto.cryptocurrency import Cryptocurrency



class Alert(ABC):
    def __init__(self, alert_id: str, type_alert: str, trigger_value: float, trigger_direction: str):
        self.alert_id = alert_id
        self.type_alert = type_alert
        self.alert_on = False
        self.sended_notice = False
        self.trigger_value = trigger_value
        self.trigger_direction = trigger_direction

    @abstractmethod
    def describe_alert(self):
        pass


    @abstractmethod
    def is_alert_on(self, current_price: float):
        pass

    def update_cryptocurrency(self, new_cryptocurrency: Cryptocurrency):
        self.cryptocurrency = new_cryptocurrency
        self.currency_name = new_cryptocurrency.currency_name
        self.currency_rate = new_cryptocurrency.currency_rate


    def update_trigger_direction(self, new_direction: str):
        self.trigger_direction = new_direction

    def update_trigger_value(self, new_trigger_value: float):
        self.trigger_value = new_trigger_value
