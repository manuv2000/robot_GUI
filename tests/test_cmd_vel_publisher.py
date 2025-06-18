# tests/test_cmd_vel_publisher.py
import unittest
from ros.cmd_vel_publisher import CmdVelPublisher

class DummyPublisher:
    def __init__(self):
        self.published = []

    def publish(self, msg):
        self.published.append(msg)

class CmdVelPublisherTestCase(unittest.TestCase):
    def test_publish(self):
        pub = CmdVelPublisher()
        pub.publisher = DummyPublisher()

        pub.publish({'linear_x': 0.5, 'angular_z': 1.0})
        msg = pub.publisher.published[0]
        
        self.assertEqual(msg.linear.x, 0.5)
        self.assertEqual(msg.angular.z, 1.0)

if __name__ == '__main__':
    unittest.main()
