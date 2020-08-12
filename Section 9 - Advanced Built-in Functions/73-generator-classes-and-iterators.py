class FirstHundredGenerator():
    def __init__(self):
        self.number = 0
        print('initialized')

    # All classes that have the dunder next method are considered generators
    def __next__(self):  # Allows you to use next(my_object)
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()


my_gen = FirstHundredGenerator()
print(next(my_gen))
print(next(my_gen))
