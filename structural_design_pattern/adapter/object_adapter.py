class OldSystem:

    def legacy_operation(self) -> str:
        return f'Legacy system operation done'


class Adapter:
    def __init__(self, old_system: OldSystem):
        self.old_system = old_system

    def operation(self):
        return f'Adapter {self.old_system.legacy_operation()}'


def client(adapter: Adapter):
    result = adapter.operation()
    print(result)


if __name__ == '__main__':
    old_system = OldSystem()
    adapter = Adapter(old_system)
    client(adapter)
