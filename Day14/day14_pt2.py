#!/usr/env/bin python3
import sys
import os
import re
import time

sys.path.append(os.path.abspath('../'))
from coordinate import Coordinate

class Robot:
    def __init__(self, pos, vel):
        self.position = pos
        self.velocity = vel

    def cycle(self, num_cycles):
        self.position = self.position + (self.velocity * num_cycles)

    def correct_position(self, width, height):
        correct = Coordinate(self.position.x % width, self.position.y % height)
        self.position = correct

def check_quadrant(robot, width, height):
    if 0 <= robot.position.x < int(width/2):
        if 0 <= robot.position.y < int(height/2):
            return 1
        elif int(height/2) < robot.position.y < height:
            return 3
    elif int(width/2) < robot.position.x < width:
        if 0 <= robot.position.y < int(height/2):
            return 2
        elif int(height/2) < robot.position.y < height:
            return 4

    return None

def map_string(robots, width, height):
    chart = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(' ')
        chart.append(row)

    for r in robots:
        chart[r.position.y][r.position.x] = '*'

    mapstr = ""
    for row in chart:
        mapstr += ''.join(row) + '\n'

    return mapstr

if __name__ == '__main__':
    robots = []

    width = 101
    height = 103

    start_cycle = int(sys.argv[2])
    end_cycle = int(sys.argv[3])

    with open(sys.argv[1]) as file:
        for line in file:
            parsed = re.match(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)', line)
            pos = Coordinate(int(parsed.group(1)),int(parsed.group(2)))
            vel = Coordinate(int(parsed.group(3)),int(parsed.group(4)))
            robot = Robot(pos,vel)
            robots.append(robot)

    for r in robots:
        r.cycle(start_cycle)
        r.correct_position(width, height)

    for c in range(start_cycle, end_cycle):
        for r in robots:
            r.cycle(1)
            r.correct_position(width, height)
        ms = map_string(robots, width, height)
        
        if '**********' in ms:
            print("\nCycle: " + str(c))
            print(ms)
            
