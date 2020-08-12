class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    # Dunder next is new to python3, so you cannot use it in python2
    # All classes that have this dunder next are called iterators
    def __next__(self):  # When defining next dunder method, you can then call next(my_object) on that object
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()


my_gen = FirstHundredGenerator()
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))


# # You cannot do this. FirstHundredGenerator is not an iterable (will look at this later)
# for i in my_gen:
#     print(i)
