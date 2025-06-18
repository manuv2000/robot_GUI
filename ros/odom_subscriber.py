import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from interfaces.subscriber_interface import RosSubscriberInterface

class OdomSubscriber(Node, RosSubscriberInterface):
    def __init__(self):
        super().__init__('odom_listener')
        self.latest_msg = None
        self.create_subscription(Odometry, '/odom', self.odom_callback, 10)

    def odom_callback(self, msg):
        self.latest_msg = msg

    def get_latest(self) -> dict:
        if self.latest_msg is None:
            return {}

        def r(x): return round(x, 3)

        return {
            "position": {
                "x": r(self.latest_msg.pose.pose.position.x),
                "y": r(self.latest_msg.pose.pose.position.y),
                "z": r(self.latest_msg.pose.pose.position.z),
            },
            "orientation": {
                "x": r(self.latest_msg.pose.pose.orientation.x),
                "y": r(self.latest_msg.pose.pose.orientation.y),
                "z": r(self.latest_msg.pose.pose.orientation.z),
                "w": r(self.latest_msg.pose.pose.orientation.w),
            },
            "twist": {
                "linear": {
                    "x": r(self.latest_msg.twist.twist.linear.x),
                    "y": r(self.latest_msg.twist.twist.linear.y),
                    "z": r(self.latest_msg.twist.twist.linear.z),
                },
                "angular": {
                    "x": r(self.latest_msg.twist.twist.angular.x),
                    "y": r(self.latest_msg.twist.twist.angular.y),
                    "z": r(self.latest_msg.twist.twist.angular.z),
                }
            }
        }
