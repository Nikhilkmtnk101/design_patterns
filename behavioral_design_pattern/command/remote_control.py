from collections import deque

from command import Command


class RemoteControl:
    """
    This is an Invoker Class which contains object of Command interface or abstract class
    """
    def __init__(self):
        self.command_history = deque()
        self.command = None

    def set_command(self, command: Command):
        self.command = command

    def press_button(self):
        self.command.execute()
        self.command_history.append(self.command)

    def undo(self):
        if len(self.command_history) != 0:
            command = self.command_history.pop()
            command.undo()
        else:
            print("command history is empty, cannot perform undo operation")

