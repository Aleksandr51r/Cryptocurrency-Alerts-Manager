from application.ports.alert_port import AlertsRepositoryPort
from application.repositories.alert_repository import InMemoryAlertsRepository


class AlertsAdapter:
    def __init__(self, repository: AlertsRepositoryPort):
        self.repository = repository

    def get_all_alert_objects(self):
        return self.repository.get_all_alert_objects()

    def get_crypto_alerts_count(self):
        return self.repository.crypto_storage.giv_me_a_count()

    def create_alert(self, type_of_alert: str, cryptocurrency: str,  trigger_value: float, trigger_direction: str):
        alert = [type_of_alert, cryptocurrency,
                 trigger_value, trigger_direction]
        self.repository.save_alert(alert)

    def get_cryptocurrency(self, cryptocurrency: str):
        return self.repository.crypto_storage.get_or_create_currency(cryptocurrency)

    def delete_alert(self, alert_id: int, cryptocurrency: str):
        self.repository.delete_alert(alert_id, cryptocurrency)

    def get_alert(self, alert_id: str):
        return self.repository.get_alert(alert_id)

    def get_all_alerts(self):
        return self.repository.get_describe_all_alerts()

    def manage_list_cryptocurrency_incresment(self, cryptocurrency: str):
        return self.repository.crypto_storage.increment_currencies_in_use(cryptocurrency)

    def manage_list_cryptocurrency_decrement(self, cryptocurrency: str):
        return self.repository.crypto_storage.decrement_currencies_in_use(cryptocurrency)
