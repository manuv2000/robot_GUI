import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from interfaces.publisher_interface import RosPublisherInterface

class CmdVelPublisher(Node, RosPublisherInterface):
    def __init__(self):
        super().__init__('cmd_vel_publisher')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)

    def publish(self, data: dict):
        msg = Twist()
        msg.linear.x = data.get('linear_x', 0.0)
        msg.angular.z = data.get('angular_z', 0.0)
        self.publisher.publish(msg)
