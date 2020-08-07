import json

file = open('csv_file.txt')
teams = [line.strip() for line in file.readlines()]
file.close()

json_teams = []

for team in teams:
    team_info = team.split(',')
    json_obj = {
        'club': team_info[0],
        'city': team_info[1],
        'country': team_info[2]
    }

    json_teams.append(json_obj)

file = open('json_file.txt', 'w')
json.dump(json_teams, file)
file.close()
