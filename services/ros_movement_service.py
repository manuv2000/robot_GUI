#deprecated
from interfaces.publisher_interface import RosPublisherInterface
from ros.cmd_vel_publisher import CmdVelPublisher
import rclpy

class ROSMovementService(RosPublisherInterface):
    def publish(self, data: dict):
        rclpy.init()
        node = CmdVelPublisher()
        node.publish(data)
        rclpy.shutdown()
        return f"Published linear_x={data.get('linear_x')}, angular_z={data.get('angular_z')}"
