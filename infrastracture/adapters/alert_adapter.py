from application.ports.alert_port import AlertsRepositoryPort

class AlertsAdapter:
    def __init__(self, alert_repository: AlertsRepositoryPort):
        self.repository = alert_repository  

# * Axillary Methods
    def get_all_alerts(self):
        return self.repository.get_all_alerts_as_objects()

# * Create Method
    def create_alert(self,  alert_data: dict):
        alert = {
            'alert_type': alert_data.get('alert_type'),
            'cryptocurrency': alert_data.get('cryptocurrency'),
            'trigger_value': alert_data.get('trigger_value'),
            'trigger_direction': alert_data.get('trigger_direction')
        }
        self.repository.save_alert(alert)

# * Read Methods
    def get_alert(self, alert_id: str):
        return self.repository.get_alert_as_obj(alert_id)

    def get_describe_all_alerts(self):
        return self.repository.get_describe_all_alerts()

# * Delete Method
    def delete_alert(self, alert_id: int, cryptocurrency: str):
        self.repository.delete_alert(alert_id, cryptocurrency)
        
