from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def fuel_type(self):
        pass

class Car(Transport):
    def move(self):
        return "Машина едет по дороге"

    def fuel_type(self):
        return "бензин"

class Bike(Transport):
    def move(self):
        return "Велосипед едет по дороге"

    def fuel_type(self):
        return "мускульная сила"

class Plane(Transport):
    def move(self):
        return "Самолёт летает"

    def fuel_type(self):
        return "керосин"