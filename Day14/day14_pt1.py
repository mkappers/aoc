#!/usr/env/bin python3
import sys
import os
import re

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

if __name__ == '__main__':
    robots = []

    width = 101
    height = 103

    with open(sys.argv[1]) as file:
        for line in file:
            parsed = re.match(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)', line)
            pos = Coordinate(int(parsed.group(1)),int(parsed.group(2)))
            vel = Coordinate(int(parsed.group(3)),int(parsed.group(4)))
            robot = Robot(pos,vel)
            robots.append(robot)

    quadrants = [0,0,0,0]
    for r in robots:
        r.cycle(100)
        r.correct_position(width, height)
        quadrant = check_quadrant(r,width,height)
        if quadrant is not None:
            quadrants[quadrant - 1] += 1
        print(r.position)

    print(quadrants)
    safety_factor = 1
    for q in quadrants:
        safety_factor *= q

    print(safety_factor)
        
