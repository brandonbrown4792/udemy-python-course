def create_account(name: str, holder: str, account_holders: list = []):
    print(id(account_holders))
    account_holders.append(holder)

    return {
        'name': name,
        'main_account_holder': holder,
        'account_holders': account_holders
    }


a1 = create_account('checking', 'Rolf')

# Here we have the account holders as Rolf and Jen
# This is because the account holders default parameter is mutable, so every time an account is created, it appends the holder to the account holders
# Never define default values for mutable data
a2 = create_account('savings', 'Jen')

print(a2)

# The way around this is to not have a default argument for lists
# Pass in an empty list on calling the function


# Alternatively, you can define the function as follows
# If no account holders list is supplied, it will create an empty list
# If account holders list is supplied, it will keep the account holders list
def create_account(name: str, holder: str, account_holders=None):
    if not account_holders:
        account_holders = []

    return {
        'name': name,
        'main_account_holder': holder,
        'account_holders': account_holders
    }
