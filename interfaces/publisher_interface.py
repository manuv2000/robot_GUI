from abc import ABC, abstractmethod
from interfaces.base.ros_translate_interface import RosTranslateInterface

class RosPublisherInterface(RosTranslateInterface, ABC):
    @abstractmethod
    def publish(self, data: dict):
        pass
