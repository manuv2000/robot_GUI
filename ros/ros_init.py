import threading
import rclpy
from ros.abstraction_node import ROSAbstractionNode

class ROSRunner:
    def __init__(self):
        # Do not init rclpy yet (simulate logic)
        self.node = ROSAbstractionNode()

    def move(self, direction: str):
        self.node.move(direction)

    def shutdown(self):
        # Placeholder for future ROS shutdown
        pass
