#!/usr/bin/env python3
import copy
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

def scan_path(scan_location, scan_movement, prev_char):
    next_scan = next_location(scan_location, scan_movement)
    next_char = lab_map[next_scan[1]][next_scan[0]]
    if next_char == 'X':
        return scan_path(next_scan, scan_movement, lab_map[scan_location[1]][scan_location[0]])
    elif next_char == '#':
        return True
    elif next_char == '.' and prev_char == '.':
        return scan_path(next_scan, scan_movement, lab_map[scan_location[1]][scan_location[0]])
    else:
        return False

obstacle_map = copy.deepcopy(lab_map)

# Movement Loop
nl = next_location(location, movement[direction])
obstructions = 0
while (nl[0] >= 0 and nl[0] < width) and (nl[1] >= 0 and nl[1] < height):
    if lab_map[nl[1]][nl[0]] == '#':
        direction = turn()
    else:
        if (lab_map[nl[1]][nl[0]] == '.') and scan_path(location, movement[turn()], '.'):
            obstacle_map[nl[1]][nl[0]] = 'O'
            obstructions += 1
        location = nl
        lab_map[nl[1]][nl[0]] = 'X'

    nl = next_location(location, movement[direction])

for row in lab_map:
    print(row)
print("---")
for row in obstacle_map:
    print(row)

num_unique = 0
for row in lab_map:
    num_unique += row.count('X')

print(num_unique)
print(obstructions)
