from abc import ABC, abstractmethod
from domain.alert.alert_ABC import Alert


class AlertsRepositoryPort(ABC):
       
# * Create Method
    @abstractmethod
    def save_alert(self, alert: Alert):
        pass

# * Read Methods
    @abstractmethod
    def get_alert_as_obj(self, alert_id: str):
        pass
    
    @abstractmethod
    def get_all_alerts_as_objects(self, alert_id: str):
        pass

    @abstractmethod
    def get_describe_all_alerts(self):
        pass

# * Delete Method
    @abstractmethod
    def delete_alert(self, alert_id: str, cryptocurrency: str):
        pass
