#!/usr/bin/env python3
import sys
import re

word_search = []
with open(sys.argv[1]) as file:
    for line in file:
        word_search.append(line.strip())

height = len(word_search)
width = len(word_search[0])

def print_block(description,block):
    print(description)
    for line in block:
        print(line)
    print("\n")

def x_block(x,y):
    block = []
    for dv in [-1,0,1]:
        block.append(word_search[y + dv][x - 1:x + 2])
    return block

def check_block(block):
    if block[1][1] != 'A':
        return False
    if (block[0][0] == 'M' and block[2][2] == 'S') or (block[0][0] == 'S' and block[2][2] == 'M'):
        if (block[2][0] == 'M' and block[0][2] == 'S') or (block[2][0] == 'S' and block[0][2] == 'M'):
            return True

    return False

x_mas_count = 0
for x in range(1, width - 1):
    for y in range(1, height - 1):
        if check_block(x_block(x,y)):
            x_mas_count += 1

print(x_mas_count)
