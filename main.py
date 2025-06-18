import rclpy
import threading
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from ros.cmd_vel_publisher import CmdVelPublisher
from ros.odom_subscriber import OdomSubscriber
from api.cmd_vel_publisher_endpoint import register_cmd_vel_routes
from api.odom_endpoint import register_odom_routes

# Initialize ROS context
rclpy.init()

# Setup FastAPI before mounting or routing
app = FastAPI()

# Mount static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Create ROS nodes
cmd_vel_node = CmdVelPublisher()
odom_node = OdomSubscriber()

# Spin odom node in a background thread
def spin_node(node):
    rclpy.spin(node)

threading.Thread(target=spin_node, args=(odom_node,), daemon=True).start()

# Register API routes
register_cmd_vel_routes(app, cmd_vel_node)
register_odom_routes(app, odom_node)
