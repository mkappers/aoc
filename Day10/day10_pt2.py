#!/usr/env/bin python3
import sys
import os
import copy

sys.path.append(os.path.abspath('../'))
from coordinate import Coordinate
from chart import Chart

directions = {'N': Coordinate(0,-1), 'E': Coordinate(1,0), 'S': Coordinate(0,1), 'W': Coordinate(-1,0)}

class HeightChart(Chart):
    def __init__(self, lines):
        super().__init__(lines)
        
        self.trailheads = self.find('0')

    def follow_trails(self):
        self.trails = {}

        for th in self.trailheads:
            trail = self.follow_trail(th)
            self.trails[th] = trail

    def follow_trail(self, curr_pos, trail = []):
        curr_value = int(self.get(curr_pos))
        new_trail = copy.copy(trail)
        new_trail.append(curr_pos)
        possible_trails = []

        if curr_value == 9:
            possible_trails.append(new_trail)

        else:
            neighbours = self.get_valid_neighbours(curr_pos)

            for nb in neighbours:
                if int(self.get(nb)) - curr_value == 1:
                    possible_trails.extend(self.follow_trail(nb, new_trail))

        return possible_trails



if __name__ == '__main__':
    # Height Map
    hc = None

    with open(sys.argv[1]) as file:
        lines = []
        for line in file:
            lines.append(line.strip())

        hc = HeightChart(lines)
   
    print("Trailheads: " + str(hc.trailheads))
    hc.follow_trails()

    uniq_dest = 0
    for th in hc.trails:
        uniq_dest += len(hc.trails[th])
    print(uniq_dest)
