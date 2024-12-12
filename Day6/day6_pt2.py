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

def mark_map(x,y):
    if lab_map[y][x] in directions:
        if direction in [0,2]:
            lab_map[y][x] = '|'
        else:
            lab_map[y][x] = '-'
    elif lab_map[y][x] == '|' and direction in [1,3]:
        lab_map[y][x] = '+'
    elif lab_map[y][x] == '-' and direction in [0,2]:
        lab_map[y][x] = '+'
    elif lab_map[y][x] == '.':
        if direction in [0,2]:
            lab_map[y][x] = '|'
        else:
            lab_map[y][x] = '-'

def turn():
    return (direction + 1) % 4

def next_location(loc_tuple, mov_tuple):
    return (loc_tuple[0] + mov_tuple[0], loc_tuple[1] + mov_tuple[1])

def print_map(m):
    for row in m:
        print(''.join(row))

# sl = scan location, sd = scan direction
def scan_line(sl,sd):
    scan_coords = []
    x,y = sl[0],sl[1]
    while x + sd[0] in range(width) and y + sd[1] in range(height):
        x = x + sd[0]
        y = y + sd[1]
        scan_coords.append(lab_map[y][x])
        if lab_map[y][x] == '#':
            break

    return scan_coords
    
# Find Start Location
for x in range(width):
    for y in range(height):
        if lab_map[y][x] in directions.keys():
            location = (x,y)
            direction = directions[lab_map[y][x]]
            break
    if location != None:
        break

#def scan_path(scan_location, scan_movement, prev_char):
#    next_scan = next_location(scan_location, scan_movement)
#    next_char = lab_map[next_scan[1]][next_scan[0]]
#    if next_char == 'X':
#        return scan_path(next_scan, scan_movement, lab_map[scan_location[1]][scan_location[0]])
#    elif next_char == '#':
#        return True
#    elif next_char == '.' and prev_char == '.':
#        return scan_path(next_scan, scan_movement, lab_map[scan_location[1]][scan_location[0]])
#    else:
#        return False

obstacle_map = copy.deepcopy(lab_map)

# Movement Loop
nl = next_location(location, movement[direction])
obstructions = 0
while (nl[0] >= 0 and nl[0] < width) and (nl[1] >= 0 and nl[1] < height):
    if lab_map[nl[1]][nl[0]] == '#':
        mark_map(location[0],location[1])
        direction = turn()
    else:
        if (lab_map[nl[1]][nl[0]] == '.'):
            scan_result = scan_line(location, movement[turn()])
            if len(scan_result) == 1 and scan_result[0] == '#':
                obstacle_map[nl[1]][nl[0]] = 'O'
                obstructions += 1

            elif scan_result[-2:] == ['+','#']:
                obstacle_map[nl[1]][nl[0]] = 'O'
                obstructions += 1
        
        mark_map(location[0],location[1])
        location = nl

    nl = next_location(location, movement[direction])

#print_map(lab_map)
#print("---")
#print_map(obstacle_map)

print("Obstructions needed: " + str(obstructions))
