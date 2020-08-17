friends = [
    {
        'name': 'Rolf',
        'location': 'Washington, D.C.'
    },
    {
        'name': 'Anna',
        'location': 'San Francisco'
    },
    {
        'name': 'Charlie',
        'location': 'San Francisco'
    },
    {
        'name': 'Jose',
        'location': 'San Francisco'
    }
]

your_location = input('Where are you right now? ')
friends_nearby = [
    friend for friend in friends if friend['location'] == your_location
]

# Any returns true for any truthy value
# Below is a list of truthy values
"""
* 0, 0.0
* None
* [], (), {}
* False
"""
# You can check if something is Falsy by running bool([arg])
if any(friends_nearby):  # True if at least none, but false if empty
    print('You are not alone!')


all([1, 2, 3, 4, 5])  # True
all([1, 2, 3, 4, 5, 0])  # False
