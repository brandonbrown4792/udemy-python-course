class Student:
  def __init__(self, name):
    self.name = name


movies = ['Matrix', 'Finding Nemo']
print(movies.__class__)
print('hi'.__class__)
print(len(movies))


class Garage:
  def __init__(self):
    self.cars = []

  def __len__(self):
    return len(self.cars)

  def __getitem__(self, i):
    return self.cars[i]

  # Every class you create should have a repr and str method
  # Repr is used for code debugging
  def __repr__(self):
    return f'<Garage {self.cars}>'

  # Str is used for runtime description
  def __str__(self):
    return f'Garage with {len(self)} cars.'

ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('Focus')

print(len(ford))
print(ford[0])

# Must have getitem method defined for this to work
for car in ford:
  print(car)

print(ford)
print(repr(ford))