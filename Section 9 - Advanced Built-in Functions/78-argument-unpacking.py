accounts = {
    'checking': 1958.00,
    'savings': 3695.50
}


def add_balance(amount: float, name: str) -> float:
    # Function to update the balance of an account and return the new balance
    accounts[name] += amount
    return accounts[name]


transactions = [
    (-180.67, 'checking'),
    (-220.00, 'checking'),
    (220.00, 'savings'),
    (-15.70, 'checking'),
    (-23.90, 'checking'),
    (-13.00, 'checking'),
    (1579.50, 'checking'),
    (-600.50, 'checking'),
    (600.50, 'savings')
]

for t in transactions:
    # This unpacks the iterables into arguments (t[0], t[1])
    # This is called argument unpacking. * is the unpacking operator
    add_balance(*t)


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, data):
        return cls(data['username'], data['password'])


# imagine these users are coming from a database...
users = [
    {'username': 'rolf', 'password': '123'},
    {'username': 'tecladoisawesome', 'password': 'youaretoo'}
]

user_objects = map(User.from_dict, users)
