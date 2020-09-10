def add_all(a1, a2, a3, a4):
    return a1 + a2 + a3 + a4

vals = (1, 3, 5, 7)

# Argument unpacking
print(add_all(*vals))


vals = {'a1': 1, 'a2': 3, 'a3': 5, 'a4': 7}

print(add_all(**vals))


# Can accept any number of arguments by using the asterisk
def add_all(*args):
    return sum(args)

print(add_all(5, 7, 3, 4))


def pretty_print(**kwargs):
    for k, v in kwargs.items():
        print(f'For {k} we have {v}.')


pretty_print(username='jose123', access_level='admin')

dic = {'username': 'jose123', 'access_level': 'admin'}
pretty_print(**dic)