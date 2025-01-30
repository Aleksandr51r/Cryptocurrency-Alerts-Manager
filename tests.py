import unittest
from infrastracture.adapters.alert_adapter import AlertsAdapter
from application.repositories.alert_repository import InMemoryAlertsRepository
from application.repositories.alert_repository import CryptocurrencyRepository


class TestAlertsAdapter(unittest.TestCase):
    def setUp(self):
        self.crypto_storage = CryptocurrencyRepository()
        self.alert_storage = InMemoryAlertsRepository(self.crypto_storage)
        self.alert_adapter = AlertsAdapter(self.alert_storage)

        # Creating initial alerts
        self.alert_adapter.create_alert('limit', "BTC", 40000, "above")
        self.alert_adapter.create_alert('limit', "Ethereum", 3000, "above")
        self.alert_adapter.create_alert('limit', "TTT", 5000, "above")
        self.alert_adapter.create_alert('persent', "BTC", 40000, "increase")
        self.alert_adapter.create_alert('persent', "Ethereum", 3000, "above")
        self.alert_adapter.create_alert('persent', "TTT", 5000, "any")

    def test_create_alerts(self):
        alerts = self.alert_adapter.get_all_alerts()
        self.assertEqual(len(alerts), 6)

    def test_crypto_alerts_count(self):
        counts = self.alert_adapter.get_crypto_alerts_count()

        self.assertEqual(counts['BTC'], 2)
        self.assertEqual(counts['ETHEREUM'], 2)
        self.assertEqual(counts['TTT'], 2)

    def test_delete_alerts(self):
        all_alert_objects = self.alert_adapter.get_all_alert_objects()
        self.alert_adapter.delete_alert(
            all_alert_objects[1].alert_id, all_alert_objects[1].cryptocurrency)
        self.alert_adapter.delete_alert(
            all_alert_objects[3].alert_id, all_alert_objects[3].cryptocurrency)

        counts = self.alert_adapter.get_crypto_alerts_count()
        print(counts)
        self.assertEqual(counts['BTC'], 1)
        self.assertEqual(counts['ETHEREUM'], 1)
        self.assertEqual(counts['TTT'], 2)

        updated_alert_objects = self.alert_adapter.get_all_alert_objects()
        self.assertEqual(len(updated_alert_objects), 4)
        print('^^^^^^^^^^^^^')
        all_alert_objects = self.alert_adapter.get_all_alert_objects()
        # print(*self.alert_adapter.get_all_alert_objects(), sep='\n')
        print(*all_alert_objects, sep='\n')

    def test_update_alert_trigger(self):
        all_alert_objects = self.alert_adapter.get_all_alert_objects()
        new_trigger_values = [11, 11, 11, 11, 11, 11]
        new_trigger_directions = ["new", "new",
                                  "new", "new", "new", "new"]
        print('^^^^^^^^^^^^^')
        # print(*self.alert_adapter.get_all_alert_objects(), sep='\n')
        print(*all_alert_objects, sep='\n')

        for i, alert in enumerate(all_alert_objects[:6]):
            alert.update_trigger_value(new_trigger_values[i])
            alert.update_trigger_direction(new_trigger_directions[i])

        for i, alert in enumerate(all_alert_objects[:6]):
            self.assertEqual(alert.trigger_value, new_trigger_values[i])
            self.assertEqual(alert.trigger_direction,
                             new_trigger_directions[i])
            
        print('$$$$$$$$')
        print(*self.alert_adapter.get_all_alert_objects(), sep='\n')


if __name__ == "__main__":
    unittest.main()
