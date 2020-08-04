# IndexError - Occurs when an index that does not exist or an index that is incorrect
friends = ['Rolf', 'Anne']
friends[2]


# KeyError - Occurs when an invalid key is accessed
movie = {
  'name': 'Matrix',
  'director': 'Lana Wachowski',
  'year': 1999
}

def show_movie_details(movie):
  print(f"Name: {movie['name']}")
  print(f"Director: {movie['director']}")
  print(f"Year: {movie['release']}")


# NameError - Occurs when python cannot find the variable or method you are trying to use
print(hello)


# AttributeError - Occurs when you try to access an attribute that is not defined
friends = ['Rolf', 'Jose', 'Charlie']
friends_nearby = ['Rolf', 'Anna'] # Cannot use intersection with lists
friends.intersection(friends_nearby)


# NotImplementedError - Use when you have not yet implemented something
class User:
  def __init__(self, username, password):
    self.username = username
    self.password = password

  def login(self):
    raise NotImplementedError('This feature has not been implemented yet')


# RuntimeError - Not really sure when this occurs. Other errors inherit from this, so this occurs whenever something else goes wrong the program


# SyntaxError - Occurs when invalid python syntax is used
class User
  def __init__(self, username, password):
    self.username = username
    self.password = password


# IndentationError - Occurs when incorrect indentation is used
def add_two(x, y):
return x + y


# TabError - Occurs when indentations are not consistent (mostly when changing between editors)
def add_two(x, y):
  return x + y

def pow(n, exp)
    return n ** exp


# TypeError - Occurs when the incorrect data type is used
5 + 'hi'


# ValueError - Occurs when you pass in the correct variable type but wrong value
int('20.5')


# ImportError - Occurs when you have circular imports or invalid import
# in app.py
import blog

def menu():
  pass

# in blog.py
from app import menu

def do_something():
  pass


# DepreciationWarning - Occurs when some part of code is depricated
class User:
  def __init__(self, username, password):
    self.username = username
    self.password = password

  def register(self):
    Database.write(self.username, self.password)
    raise DeprecationWarning('User#register still works, but is depricated.')

  @classmethod
  def register_user(cls, username, password):
    Database.write(username, password)
    return cls(username, password)