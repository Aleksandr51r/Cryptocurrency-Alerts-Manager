
from infrastracture.adapters.alert_adapter import AlertsAdapter
from application.repositories.alert_repository import InMemoryAlertsRepository
from application.repositories.alert_repository import CryptocurrencyRepository
from cli.cli import alerts_manager


def main():
    crypto_storage = CryptocurrencyRepository()
    alert_storage = InMemoryAlertsRepository(crypto_storage)
    alert_adapter = AlertsAdapter(alert_storage)

    alerts_manager(obj={"alert_adapter": alert_adapter})


if __name__ == '__main__':
    main()
