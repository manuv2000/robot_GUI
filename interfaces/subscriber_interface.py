from abc import ABC, abstractmethod
from interfaces.base.ros_translate_interface import RosTranslateInterface

class RosSubscriberInterface(RosTranslateInterface, ABC):
    @abstractmethod
    def get_latest(self) -> dict:
        pass
