from domain.alert.alert_by_limit import Alert_by_limit
from domain.alert.alert_by_percent import Alert_by_percent
from application.ports.alert_port import AlertsRepositoryPort
from application.repositories.crypto_repository import CryptocurrencyRepository

from random import choices
import string


class InMemoryAlertsRepository(AlertsRepositoryPort):
    def __init__(self, crypto_storage: CryptocurrencyRepository):
        self.alerts = {}
        self.crypto_storage = crypto_storage

    def get_all_alert_objects(self):
        return list(self.alerts.values())

    def generate_unique_id(self):
        while True:
            new_id = ''.join(choices(string.ascii_uppercase, k=2))
            if new_id not in self.alerts:
                return new_id

    def get_alert(self, alert_id: str):
        return self.alerts.get(alert_id)

    def get_describe_all_alerts(self):
        return [alert.describe_alert() for alert in self.alerts.values()]

    def save_alert(self, alert_list):

        alert_id = self.generate_unique_id()
        alert_type = alert_list[0]
        user_input_cryptocurrency = alert_list.pop(1)
        cryptocurrency_id = self.crypto_storage.get_or_create_currency(
            user_input_cryptocurrency)
        print('REPO', cryptocurrency_id)

        alert_list.insert(1, cryptocurrency_id)
        alert_list.insert(0, alert_id)

        # ! Alert arg  :
        # ! alert_id, type_alert, cryptocurrency_id,
        # ! trigger_value, trigger_direction

        if alert_type == 'limit':
            alert = Alert_by_limit(*alert_list)
        else:
            alert = Alert_by_percent(*alert_list)

        self.alerts[alert_id] = alert
        self.crypto_storage.increment_currencies_in_use(alert.cryptocurrency)

    def delete_alert(self, alert_id: str, cryptocurrency: str):
        self.crypto_storage.decrement_currencies_in_use(cryptocurrency)
        del self.alerts[alert_id]
