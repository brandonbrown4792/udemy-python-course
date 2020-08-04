import random

# This line creates a set with 6 random numbers
lottery_numbers = set(random.sample(range(22), 6))

# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]

max_matching = 0
max_player = players[0]

for player in players:
  num_matching = len(lottery_numbers.intersection(player['numbers']))
  if num_matching > max_matching:
    max_player = player
    max_matching = num_matching

print(f"{max_player['name']} won {100 ** max_matching}")