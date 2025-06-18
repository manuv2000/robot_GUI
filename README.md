# Robot Interface: Web GUI for Mobile Robot (ROS 2 + FastAPI)

- A FastAPI-based backend
- A simple HTML/JavaScript GUI for manual movement commands
- Real-time odometry updates
- Containerized development and simulation environment (via Docker Compose)

---

## Current Functionality

- Publish velocity commands (`/cmd_vel`) via GUI buttons (Forward / Backward / Turn).
- Subscribe to odometry data (`/odom`) and display it live in the interface.
- Modular interface design based on publisher/subscriber abstractions.
- ROS 2 + FastAPI integration tested in simulation with **Gazebo** container.
- Auto-refresh odometry every second via JS polling.

---

## Planned Improvements

> See [Dalsze kierunki rozwoju projektu](#) in the full report for detailed goals.

- Implement support for `/joint_states` to observe and control robot joints (e.g. UR5 arm).
- Subscriptions to additional telemetry: LIDAR (`/scan`), cameras, diagnostic topics.
- Move from simulated to real robot (`Robot 4.0`) testing.
- Add user input validation, safety stops, and test coverage (unit + integration).
- WebSocket-based live updates to reduce latency.
- Extend GUI with data logs and real-time 2D/3D robot pose visualization.

---

## Docker-Based Architecture

This project uses Docker Compose to run the full simulation + interface environment in isolated containers:

| Container         | Purpose                                         |
|------------------|--------------------------------------------------|
| `robot-fastapi`   | FastAPI backend + ROS 2 client node (`cmd_vel` + `odom`) |
| `robot40-ros2-dev`| ROS 2 + Gazebo simulator exposing relevant topics |

All containers are connected via a **custom bridge network** to enable seamless ROS 2 DDS communication (via shared `ROS_DOMAIN_ID`).

---

## Prerequisites

Ensure the following are set up **before launching**:

1. **Docker & Docker Compose** installed  
   → [Docker Installation Guide](https://docs.docker.com/get-docker/)
   changing the paths leading to project files

3. **X11 Forwarding (Linux GUI)** for Gazebo visualization:
   ```bash
   xhost +local:root
