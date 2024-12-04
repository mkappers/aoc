#!/usr/bin/env python3
import sys
import re

word_search = []
with open(sys.argv[1]) as file:
    for line in file:
        word_search.append(line.strip())

height = len(word_search)
width = len(word_search[0])
diagonal = min(height, width)

#print("Horizontal")
#for line in word_search:
#    print(line)

flipped_search = []
for i in range(len(word_search[0])):
    column = [word_search[x][i] for x in range(len(word_search))]
    flipped_search.append(''.join(column))

#print("\n Vertical")
#for line in flipped_search:
#    print(line)

# Diagonal Search Topleft to Bottomright
# Start of each line: X = 0 OR Y = 0
# Vector: (+1, +1)
tl_br_start = []
for x in range(width-1,0,-1):
    tl_br_start.append((x,0))
for y in range(height):
    tl_br_start.append((0,y))

tl_br_search = []
for line_start in tl_br_start:
    tl_br_line = []
    for i in range(diagonal):
        x = line_start[0] + i
        y = line_start[1] + i
        if x < width and y < height:
            tl_br_line.append(word_search[y][x])
        else:
            continue

    tl_br_search.append(''.join(tl_br_line))

#print("\nDiagonal")
#for start in tl_br_start:
#    print(start)
#
#print("\nLines")
#for line in tl_br_search:
#    print(line)

# Diagonal Search Bottomleft to Topright
# Start of each line: X = 0 OR Y = N
# Vector: (+1, -1)
bl_tr_start = []
for y in range(height):
    bl_tr_start.append((0,y))
for x in range(1, width):
    bl_tr_start.append((x, height-1))

bl_tr_search = []
for line_start in bl_tr_start:
    bl_tr_line = []
    for i in range(diagonal):
        x = line_start[0] + i
        y = line_start[1] - i
        if x < width and y >= 0:
            bl_tr_line.append(word_search[y][x])
        else:
            continue

    bl_tr_search.append(''.join(bl_tr_line))

#print("\nDiagonal")
#for start in bl_tr_start:
#    print(start)
#
#print("\nLines")
#for line in bl_tr_search:
#    print(line)

# FINALLY THE ACTUAL COUNTING
xmas_count = 0
for search in [word_search,flipped_search,tl_br_search,bl_tr_search]:
    for line in search:
        xmas_count += line.count("XMAS")
        xmas_count += line.count("SAMX")

print(xmas_count)

