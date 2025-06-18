FROM osrf/ros:humble-desktop-jammy

# Set noninteractive mode to avoid prompts
ENV DEBIAN_FRONTEND=noninteractive

# Update and install Python tooling
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-colcon-common-extensions \
    python3-vcstool \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install FastAPI and uvicorn
RUN pip3 install fastapi uvicorn jinja2 python-multipart

# Set working directory and copy app
COPY ./ /app
WORKDIR /app
ENV PYTHONPATH=/app
ENV ROS_DOMAIN_ID=40


# Default command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc