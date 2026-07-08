# ABC -> abstract based class

from abc import ABC, abstractmethod

# abc is a module

# class Animal(ABC):
#     @abstractmethod

#     def sound(self):
#         pass

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# obj = Dog()
# obj.sound()


# Multiple abstraction

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    def stop(self):
        pass

class Bike(Vehicle):
    def start(self):
        print("Bike Start")

    def stop(self):
        print("Bike Stop")

obj = Bike()
obj.start()
obj.stop()