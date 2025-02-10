from domain.alert.alert_by_limit import Alert_by_limit
from domain.alert.alert_by_percent import Alert_by_percent
from application.ports.alert_port import AlertsRepositoryPort
from application.repositories.crypto_repository import CryptocurrencyRepository
from tools import generate_unique_id


class AlertsRepository(AlertsRepositoryPort):
    def __init__(self, crypto_storage: CryptocurrencyRepository):
        self.alerts = {}  # { alert_id: Alert(obj) }
        # ! Only here where we link crypto_storage whith AlertsRepository
        self.crypto_storage = crypto_storage

# * Axillary Methods
    def get_all_alerts_as_objects(self):
        return list(self.alerts.values())


# * Create Method

    def save_alert(self, alert: dict):

        alert_id = generate_unique_id()
        while alert_id in self.alerts:
            alert_id = generate_unique_id()

        alert_type = alert['alert_type']
        
        # ! print(alert)
        # ! {'alert_type': 'limit', 'cryptocurrency': 'BTC', 'trigger_value': 105000, 'trigger_direction': 'below'}
        
        user_input_cryptocurrency = alert.pop('cryptocurrency')
        cryptocurrency_id = self.crypto_storage.get_or_create_currency(user_input_cryptocurrency)
        alert['cryptocurrency_id'] = cryptocurrency_id
        alert['alert_id'] = alert_id

        # ! print(alert)
        # ! {'alert_type': 'limit', 'trigger_value': 500, 'trigger_direction': 'above', 'cryptocurrency_id': <domain.crypto.cryptocurrency.Cryptocurrency object at 0x000001927E68EB60>, 'alert_id': 'ON'}

        if alert_type == 'limit':
            alert_obj = Alert_by_limit(alert['alert_id'], alert['alert_type'],
                                       alert['cryptocurrency_id'], alert['trigger_value'], alert['trigger_direction'])
        elif alert_type == 'percent':
            try:
                alert_obj = Alert_by_percent(alert['alert_id'], alert['alert_type'],
                                             alert['cryptocurrency_id'], alert['trigger_value'], alert['trigger_direction'])
            except Exception as e:  # General exception for any other errors
                print(f"Error: {e} - Something went wrong")
        else:
            print(
                f"It's impossible create the alert type for {alert['cryptocurrency_id']}")
            raise ValueError(f"Unknown alert type: {alert_type}")

        print(alert_obj)

        self.alerts[alert_id] = alert_obj
        self.crypto_storage.increment_currencies_in_use(
            alert_obj.cryptocurrency)


# * Read Methods

    def get_alert_as_obj(self, alert_id: str):
        return self.alerts.get(alert_id)
    def get_describe_all_alerts(self):
        return [alert.describe_alert() for alert in self.alerts.values()]

# * Delete Method
    def delete_alert(self, alert_id: str, cryptocurrency: str):
        self.crypto_storage.decrement_currencies_in_use(cryptocurrency)
        del self.alerts[alert_id]
