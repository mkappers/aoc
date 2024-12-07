#!/usr/bin/env python3
import sys
import re

lab_map = []
with open(sys.argv[1]) as file:
    for line in file:
        row = []
        for character in line.strip():
            row.append(character)

        lab_map.append(row)

height = len(lab_map)
width = len(lab_map[0])

#for row in lab_map:
#    print(row)

# Up, Right, Down, Left
directions = {'^': 0, '>':1, 'v':2, '<':3}
movement = [(0,-1),(1,0),(0,1),(-1,0)]
location = None
direction = None

# Find Start Location
for x in range(width):
    for y in range(height):
        if lab_map[y][x] in directions.keys():
            location = (x,y)
            direction = directions[lab_map[y][x]]
            lab_map[y][x] = 'X'
            break
    if location != None:
        break

def turn():
    return (direction + 1) % 4

def next_location(loc_tuple, mov_tuple):
    return (loc_tuple[0] + mov_tuple[0], loc_tuple[1] + mov_tuple[1])

# Movement Loop
nl = next_location(location, movement[direction])
while (nl[0] >= 0 and nl[0] < width) and (nl[1] >= 0 and nl[1] < height):
    if lab_map[nl[1]][nl[0]] == '#':
        direction = turn()
    else:
        location = nl
        lab_map[nl[1]][nl[0]] = 'X'

    nl = next_location(location, movement[direction])

for row in lab_map:
    print(row)

num_unique = 0
for row in lab_map:
    num_unique += row.count('X')

print(num_unique)
