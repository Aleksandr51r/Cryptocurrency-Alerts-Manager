from domain.crypto.cryptocurrency import Cryptocurrency
from domain.alert.alert_ABC import Alert
from cli import description_id, user_choose, description_status


class Alert_by_limit(Alert, Cryptocurrency):
    def __init__(self, alert_id: str, alert_type: str, cryptocurrency_id: Cryptocurrency, trigger_value: float, trigger_direction: str):
        Alert.__init__(self, alert_id, alert_type,
                       trigger_value, trigger_direction)
        Cryptocurrency.__init__(self, cryptocurrency_id.cryptocurrency_id,
                                cryptocurrency_id.currency_name, cryptocurrency_id.currency_rate)
        self.cryptocurrency = cryptocurrency_id
        self.description = self.describe_alert()

# * Principales methods

    def describe_alert(self):
        status = "ACTIVATE" if self.is_alert_on(
            self.currency_rate) else "INACTIVE"
        return f"ALERT ID: {description_id(self.alert_id)} | STATUS: {description_status(status)} | Actual rate \033[44m{self.currency_rate}\033[0m | CONDITION: If {user_choose(self.cryptocurrency.cryptocurrency_id)}'s ({user_choose(self.cryptocurrency.currency_name)}) rate will be {user_choose(self.trigger_direction)} than {user_choose(self.trigger_value)} $."

    def is_alert_on(self, current_price: float):
        """
        Realises the primary function of the alert system to check if a price has passed a limit
        (either increased or decreased) in the specified direction.

        Args:
                current_price (float): The current price of the cryptocurrency.
                trigger_direction (str): The direction to monitor ("above" or "below").
                trigger_value (float): The price value that triggers the alert.
        Returns:
                bool: Returns True if the price has passed the trigger value in the specified direction, otherwise False.
        """

        if self.trigger_direction == 'above' and current_price > self.trigger_value or self.trigger_direction == 'below' and current_price < self.trigger_value:
            self.alert_on = True
            if self.sended_notice == False:
                'send notation here'
                self.sended_notice = True
        else:
            self.alert_on = False
            self.sended_notice = False

        return self.alert_on


# * Modifying methods initialized in ABC

    def __str__(self):
        return self.describe_alert()
        return f"Alert Number {self.alert_id} for {self.cryptocurrency} {self.trigger_direction} {self.trigger_value} $"
