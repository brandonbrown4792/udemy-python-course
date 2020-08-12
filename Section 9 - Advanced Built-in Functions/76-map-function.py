friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Mary']
start_with_r = filter(lambda friend: friend.startswith('R'), friends)

another_starts_with_r = (f for f in friends if f.startswith('R'))

# These are identical, but you should use the second
friends_lower = map(lambda x: x.lower(), friends)
friends_lower = (friend.lower() for friend in friends)

for friend in friends_lower:
    print(friend)
