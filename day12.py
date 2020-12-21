import re

#filename = 'day12_test.txt'
filename = 'day12.txt'

instructions = open(filename, 'r').read().split('\n')

distance = {'N':0, 'E':0, 'S':0, 'W':0}
direction = 'E'
heading = 90

for instruction in instructions:
    instr = re.findall(r'(\w+?)(\d+)', instruction)[0]
    command = instr[0]
    val = int(instr[1])
    if command == 'F':
        distance.update({direction:distance[direction] + val})
    elif command == 'N':
        distance.update({'N':distance['N'] + val})
    elif command == 'E':
        distance.update({'E':distance['E'] + val})
    elif command == 'S':
        distance.update({'S':distance['S'] + val})
    elif command == 'W':
        distance.update({'W':distance['W'] + val})
    elif command == 'R':
        heading += val
    elif command == 'L':
        heading -= val
    else:
        print('command not understood:', command)
    if command in ['R', 'L']:
        heading = heading % 360
        if heading == 0:
            direction = 'N'
        elif heading == 90:
            direction = 'E'
        elif heading == 180:
            direction = 'S'
        elif heading == 270:
            direction = 'W'
        else:
            print('Heading not understood:', heading)

print(distance)
vertical = distance['N'], distance['S']
horisontal = distance['E'], distance['W']

travel = max(vertical) - min(vertical) + max(horisontal) - min(horisontal)
print('Manhattan distance:',travel)

#####  Part two  #####

waypoint = {'N':1, 'E':10}
ship = {'N':0, 'E':0}

for instruction in instructions:
    instr = re.findall(r'(\w+?)(\d+)', instruction)[0]
    command = instr[0]
    val = int(instr[1])
    N = waypoint['N']
    E = waypoint['E']
    if command == 'F':
        northwards = N * val
        eastwards = E * val
        ship.update({'N':ship['N'] + northwards, 'E':ship['E'] + eastwards})
    elif command == 'N':
        waypoint.update({'N':N + val})
    elif command == 'E':
        waypoint.update({'E':E + val})
    elif command == 'S':
        waypoint.update({'N':N - val})
    elif command == 'W':
        waypoint.update({'E':E - val})
    elif command in ['R', 'L']:
        turn = val % 360
        if turn == 90:
            if command == 'R':
                waypoint.update({'N':-E, 'E':N})
            else:
                waypoint.update({'N':E, 'E':-N})
        elif turn == 180:
            waypoint.update({'N':-N, 'E':-E})
        elif turn == 270:
            if command == 'R':
                waypoint.update({'N':E, 'E':-N})
            else:
                waypoint.update({'N':-E, 'E':N})

vertical_distance = abs(ship['N'])
horisontal_distance = abs(ship['E'])
manhattan_distance = vertical_distance + horisontal_distance
print('Manhattan distance (part two):', manhattan_distance)
