"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):

    def __init__(self, weight: int, fuel: int, fuel_consumption: int, max_cargo: int):
        Vehicle.__init__(self, weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, cargo):
        if self.max_cargo >= cargo:
            self.cargo = cargo
        else:
            raise CargoOverload("Cargo overload")

    def remove_all_cargo(self):
        saved_value = self.cargo
        self.cargo = 0
        return saved_value

