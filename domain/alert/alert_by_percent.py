from domain.crypto.cryptocurrency import Cryptocurrency
from domain.alert.alert_ABC import Alert
from cli import description_id, user_choose, description_status


class Alert_by_percent(Alert, Cryptocurrency):
    def __init__(self, alert_id: str, type_alert, cryptocurrency_id: Cryptocurrency, trigger_value: float, trigger_direction: str):
        Alert.__init__(self, alert_id, type_alert, trigger_value,trigger_direction)
        Cryptocurrency.__init__(self, cryptocurrency_id.cryptocurrency_id, cryptocurrency_id.currency_name, cryptocurrency_id.currency_rate)
        self.cryptocurrency = cryptocurrency_id
        self.description = self.describe_alert()

# * Principales methods

    def describe_alert(self):
        status = "ACTIVATE" if self.is_alert_on(self.currency_rate) else "INACTIVE"
        return f"Alert ID: {description_id(self.alert_id)} | STATUS: {description_status(status)} | Alert will be activated if the rate of {user_choose(self.cryptocurrency)} changes by {user_choose(self.trigger_value)} % in {user_choose('increase or decrease') if self.trigger_direction == 'any' or self.trigger_direction == '' else user_choose(self.trigger_direction)}."

    def is_alert_on(self, current_price: float, trigger_direction: str = None):
        """
        Checks if the alert is activated based on the percentage change.

        Args:
            current_price (float): The current price of the cryptocurrency.
            trigger_direction (str, optional): The direction of the price change ("increase" or "decrease").
                                            If not specified, the alert will trigger on any change (both increase or decrease).
        Returns:
            bool: True if the alert is activated, False otherwise.
        """

        rate_change = self.cryptocurrency_rate - self.trigger_value
        percent_change = (rate_change / self.trigger_value) * 100

        if trigger_direction is None:
            self.alert_on = abs(percent_change) >= self.trigger_value
        elif trigger_direction == "increase" and percent_change >= self.trigger_value:
            self.alert_on = True
        elif trigger_direction == "decrease" and percent_change <= -self.trigger_value:
            self.alert_on = True
        else:
            self.alert_on = False

        return self.alert_on

# * Modifying methods initialized in ABC

    def __str__(self):
        return self.describe_alert()
        return f"Alert ID {self.alert_id} for {self.cryptocurrency} in change of {self.trigger_direction} direction {self.trigger_value} %"
