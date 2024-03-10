from abc import ABC, abstractmethod

from air_condtion import AirCondition

"""
This module contains commands which will be invoked by Client
"""


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class TurnOnAcCommand(Command):
    def __init__(self, air_condition: AirCondition):
        self._air_condition = air_condition

    def execute(self):
        self._air_condition.turn_on_ac()

    def undo(self):
        self._air_condition.turn_off_ac()


class TurnOffAcCommand(Command):
    def __init__(self, air_condition: AirCondition):
        self._air_condition = air_condition

    def execute(self):
        self._air_condition.turn_off_ac()

    def undo(self):
        self._air_condition.turn_on_ac()
