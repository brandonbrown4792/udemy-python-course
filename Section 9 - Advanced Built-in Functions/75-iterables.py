class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()

    def __iter__(self):
        return self


print(sum(FirstHundredGenerator()))

for i in FirstHundredGenerator():
    print(i)


# You can define an iterable class by either using the __iter__ method or __len__ and __getitem__ methods
# Iterator is used to get the next value
# Iterable is used to go over all the values of the iterator
class AnotherIterable:
    def __init__(self):
        self.cars = ['Fiesta', 'Focus']

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]


for car in AnotherIterable():
    print(car)
