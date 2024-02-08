class Car:
    """Базовый класс машины"""
    def __init__(self, model: str, power: int, weight: int) -> None:
        """
        Конструктор класса Car.

        Параметры:
        - model: str - модель машины
        - power: int - мощность машины
        - weight: int - масса машины

        """
        self._model = model
        self.power = power
        self.weight = weight

    @property
    def model(self) -> str:
        """Геттер, который делает переменную model непубличной, так как машина не может поменять свою модель"""
        return self._model

    def __str__(self) -> str:
        return f"Машина {self.model}. Мощность {self.power}. Масса {self.weight}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(model={self.model!r}, power={self.power!r}, weight={self.weight!r})"

    def horsepower(self) -> float:
        """
        Функция, которая считает лошадиные силы машины

        """
        return self.power * 1.4

    def max_weight_car(self) -> int:
        """
        Функция, которая считает максимальную массу машины

        """
        return self.weight


class PassengerCar(Car):
    """Дочерний класс легковой автомобиль"""
    def __init__(self, model: str, power: int, weight: int, passengers: int) -> None:
        """
        Конструктор класса PassengerCar.

        Параметры:
        - model: str - модель машины
        - power: int - мощность машины
        - weight: int - масса машины
        - passengers: int - максимальное количество пассажиров

        """
        super().__init__(model, power, weight)
        self.passengers = passengers

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(model={self.model!r}, power={self.power!r}, weight={self.weight!r}, passengers={self.passengers!r})"

    def max_weight_car(self) -> int:
        """
        Функция, которая считает максимальную массу машины
        Функция перегружена, так как в легковой машине могут находиться пассажиры, которые добавляют массу машине

        """
        return self.weight + self.passengers * 70


class Trucks(Car):
    """Дочерний класс грузовой автомобиль"""
    def __init__(self, model: str, power: int, weight: int, carrying: int) -> None:
        """
        Конструктор класса Trucks.

        Параметры:
        - model: str - модель машины
        - power: int - мощность машины
        - weight: int - масса машины
        - carrying: int - максимальное количество пассажиров

        """
        super().__init__(model, power, weight)
        self.carrying = carrying

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(model={self.model!r}, power={self.power!r}, weight={self.weight!r}, passengers={self.carrying!r})"

    def max_weight_car(self) -> int:
        """
        Функция, которая считает максимальную массу машины
        Функция перегружена, так как в грузовой машине может находиться груз, который добавит массу машине

        """
        return self.weight + self.carrying


if __name__ == "__main__":
    clcar = Car("Lada", 100, 2000)
    print(clcar)
    passengercar = PassengerCar("Lada", 100, 2000, 5)
    print(passengercar)
    trucks = Trucks("Lada", 100, 2000, 1000)
    print(trucks)
    pass
