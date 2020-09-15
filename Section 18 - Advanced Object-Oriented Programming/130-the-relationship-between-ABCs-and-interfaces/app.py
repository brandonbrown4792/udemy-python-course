from admin import Admin
from database import Database
from user import User

a = Admin('rolf', '1234', 3)
u = User('jose', 'password')

users = [u, a]

for user in users:
    user.save()

for user in users:
    print(user.to_dict())
