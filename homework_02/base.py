from abc import ABC
from homework_02.exceptions import NotEnoughFuel, LowFuelError


class Vehicle(ABC):
    def __init__(self, weight: int, fuel: int, fuel_consumption: int):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if self.fuel > 0:
            self.started = True
        else:
            raise LowFuelError("Low Fuel for start")

    def move(self, distance_length):
        if (self.fuel_consumption * distance_length) > self.fuel:
            raise NotEnoughFuel("Not enough fuel")
        else:
            self.fuel = self.fuel - (self.fuel_consumption * distance_length)