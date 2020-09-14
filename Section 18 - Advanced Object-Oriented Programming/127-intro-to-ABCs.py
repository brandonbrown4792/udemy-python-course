# ABC means abstract base class
from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    def walk(self):
        print('Walking...')

    @abstractmethod
    def num_legs(self):
        pass


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def num_legs(self):
        return 4


class Monkey(Animal):
    def __init__(self, name):
        self.name = name

    def num_legs(self):
        return 2


class Whale(Animal):
    pass


# # This will throw an error because abstract methods tell Python that we do not want to use the Animal class
# a = Animal()
# print(a.num_legs())

# # If you try to create an object with a class that does not have the abstracted method defined, you will get an error
# w = Whale()

d = Dog('Scooby')
