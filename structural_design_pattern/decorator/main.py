from abc import ABC, abstractmethod


class BasePizza(ABC):
    @abstractmethod
    def cost(self) -> int:
        pass


class MargheritaPizza(BasePizza):
    def cost(self) -> int:
        return 100


class FarmHousePizza(BasePizza):
    def cost(self) -> int:
        return 200


class VegDelight(BasePizza):
    def cost(self) -> int:
        return 300


class PizzaDecorator(BasePizza):
    def __init__(self, base_pizza: BasePizza):
        self._base_pizza = base_pizza

    def cost(self) -> int:
        return self._base_pizza.cost()


class ExtraCheese(PizzaDecorator):
    def __init__(self, base_pizza):
        super(ExtraCheese, self).__init__(base_pizza=base_pizza)

    def cost(self) -> int:
        return super(ExtraCheese, self).cost() + 10


class Mushroom(PizzaDecorator):
    def __init__(self, base_pizza):
        super(Mushroom, self).__init__(base_pizza=base_pizza)

    def cost(self) -> int:
        return super(Mushroom, self).cost() + 20


def client_fun(pizza: BasePizza):
    print("cost of pizza is ", pizza.cost())


if __name__ == '__main__':
    pizza = Mushroom(ExtraCheese(FarmHousePizza()))
    client_fun(pizza)

