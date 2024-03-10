from air_condtion import AirCondition
from command import TurnOnAcCommand
from remote_control import RemoteControl

if __name__ == "__main__":
    air_condition = AirCondition()
    turn_on_ac_command = TurnOnAcCommand(air_condition)
    remote_control = RemoteControl()
    remote_control.set_command(turn_on_ac_command)

    remote_control.press_button()
    remote_control.undo()
    remote_control.undo()
