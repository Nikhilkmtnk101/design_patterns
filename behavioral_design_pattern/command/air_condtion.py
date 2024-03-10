class AirCondition:
    """
    This is a Receiver Class.
    """
    def __init__(self):
        self._is_on = False
        self._temp = 0

    def turn_on_ac(self):
        print("Turning on the ac")
        self._is_on = True

    def turn_off_ac(self):
        print("Turning off the ac")
        self._is_on = False

    def set_temp(self, temp: int):
        print(f'Setting temperature of ac to {temp}')
        self._temp = temp

    def get_temp(self) -> int:
        return self._temp

