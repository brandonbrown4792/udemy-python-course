accounts = {
    'checking': 1958.00,
    'savings': 3695.50
}


# Default value of checking if name is not provided
# Default valued arguments must be at the end of the arguments declaration
def add_balance(amount: float, name: str = 'checking') -> float:
    # Function to update the balance of an account and return the new balance
    accounts[name] += amount
    return accounts[name]


add_balance(500, 'savings')
print(accounts['checking'])
print(accounts['savings'])

add_balance(500)
print(accounts['checking'])
print(accounts['savings'])
