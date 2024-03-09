from abc import ABC, abstractmethod

from sprites import Sprites
from constants import RobotTypes


class Robot(ABC):
    @abstractmethod
    def display(self, x: int, y: int):
        pass

    @abstractmethod
    def get_type(self) -> str:
        pass

    @abstractmethod
    def get_body(self) -> str:
        pass


class HumanoidRobot(Robot):
    """
    This class should be immutable class so making variables to private and not creating setter method
    """
    def __init__(self, sprites: Sprites):
        print("Taking 31 kb to create object")
        self._type = RobotTypes.HUMANOID.value
        self._body = sprites

    def display(self, x: int, y: int):
        print(f'Displaying Human Robot at x: {x} and y: {y}')

    def get_type(self) -> str:
        return self._type

    def get_body(self) -> Sprites:
        return self._body


class AnimalRobot(Robot):
    """
    This class should be immutable class so making variables to private and not creating setter method
    """
    def __init__(self, sprites: Sprites):
        print("Taking 31 kb to create object")
        self._type = RobotTypes.ANIMAL.value
        self._body = sprites

    def display(self, x: int, y: int):
        print(f'Displaying Animal Robot at x: {x} and y: {y}')

    def get_type(self) -> str:
        return self._type

    def get_body(self) -> Sprites:
        return self._body
