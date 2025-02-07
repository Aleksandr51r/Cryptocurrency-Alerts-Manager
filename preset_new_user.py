from infrastracture.adapters.alert_adapter import AlertsAdapter
from application.repositories.alert_repository import AlertsRepository
from application.repositories.crypto_repository import CryptocurrencyRepository


class New_User:
    def __init__(self):
        self.crypto_storage = CryptocurrencyRepository()
        self.alert_storage = AlertsRepository(self.crypto_storage)
        self.alert_adapter = AlertsAdapter(self.alert_storage)

        alert_presets = [
            {
                'alert_type': 'limit',
                'cryptocurrency': 'BTC',
                'trigger_value': 45000,
                'trigger_direction': 'above'
            },
            {
                'alert_type': 'limit',
                'cryptocurrency': 'ETH',
                'trigger_value': 3000,
                'trigger_direction': 'below'
            },
            {
                'alert_type': 'limit',
                'cryptocurrency': 'BNB',
                'trigger_value': 500,
                'trigger_direction': 'above'
            },
            # {
            #     'alert_type': 'limit',
            #     'cryptocurrency': 'SOL',
            #     'trigger_value': 100,
            #     'trigger_direction': 'below'
            # },
            # {
            #     'alert_type': 'limit',
            #     'cryptocurrency': 'ADA',
            #     'trigger_value': 1.5,
            #     'trigger_direction': 'above'
            # },
            # {
            #     'alert_type': 'limit',
            #     'cryptocurrency': 'XRP',
            #     'trigger_value': 0.8,
            #     'trigger_direction': 'below'
            # }
        ]

        for alert_data in alert_presets:
            self.alert_adapter.create_alert(alert_data)
