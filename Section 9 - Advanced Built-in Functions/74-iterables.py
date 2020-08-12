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


# Creating the __iter__ method allows python to iterate over a iterator (you are creating an iterable for the iterator)
class FirstHundredIterable:
    def __iter__(self):
        return FirstHundredGenerator()


# You can now iterate over the iterable that was created from the iterator
print(sum(FirstHundredIterable()))

for i in FirstHundredIterable():
    print(i)


# Alternatively, you can create the iterable inside the generator itself
class FirstThousandGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 1000:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()

    def __iter__(self):
        return self


print(sum(FirstThousandGenerator()))

for i in FirstThousandGenerator():
    print(i)


# You can also define an iterable by using __len__ and __getitem__ together
class AnotherIterable:
    def __init__(self):
        self.cars = ['Fiesta', 'Focus']

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]


for car in AnotherIterable():
    print(car)


# An iterator is used to get the next value (step by step)
# An iterable is used to go over all the values of the iterator (the whole shabang)


# You can shorthand create an iterator by using the syntax below
my_numbers = [x for x in [1, 2, 3, 4, 5]]

# This is not a tuple. This is called a generator comprehension
my_numbers_gen = (x for x in [1, 2, 3, 4, 5])


g = my_numbers_gen
print(next(g))
print(next(g))
print(next(g))
