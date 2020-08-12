class PrimeGenerator:
    # You may modify the __init__() method if necessary, but you don't need to change its arguments
    def __init__(self, stop):
        # stop defines the range (exclusive upper bound) in which we search for the primes
        self.stop = stop
        self.num = 2

    def __next__(self):
        for n in range(self.num, self.stop):
            for x in range(2, n):
                if n % x == 0:
                    break
            else:
                self.num = n + 1
                return n
        raise StopIteration()


my_object = PrimeGenerator(42)

print(next(my_object))
print(next(my_object))
print(next(my_object))
