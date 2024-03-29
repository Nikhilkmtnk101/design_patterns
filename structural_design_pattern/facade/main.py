class CPU:
    def freeze(self):
        print("Freezing processor.")

    def jump(self, position: str):
        print("Jumping to: ", position)

    def execute(self):
        print("Executing.")


class Memory:
    def load(self, position: str, data: str) -> None:
        print(f"Loading from {position} data: '{data}'.")


class SolidStateDrive:
    def read(self, lba: str, size: str) -> str:
        return f"Some data from sector {lba} with size {size}"


class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.ssd = SolidStateDrive()

    def start(self):
        self.cpu.freeze()
        self.memory.load("0x00", self.ssd.read("100", "1024"))
        self.cpu.jump("0x00")
        self.cpu.execute()


if __name__ == "__main__":
    c = ComputerFacade()
    c.start()
