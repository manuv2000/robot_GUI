#deprecated
from ros.odom_subscriber import OdomSubscriber

class OdomListenerService:
    def __init__(self):
        self.subscriber_node = OdomSubscriber() 
    def get_odom_data(self) -> dict:
        return self.subscriber_node.get_latest()