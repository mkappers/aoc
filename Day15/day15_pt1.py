#!/usr/env/bin python3
import sys
import os

sys.path.append(os.path.abspath('../'))
from coordinate import Coordinate
from chart import Chart

directions = {'^': Coordinate(0,-1), '>': Coordinate(1,0), 'v': Coordinate(0,1), '<': Coordinate(-1,0)}

class BoxChart(Chart):
    def __init__(self, lines):
        super().__init__(lines)
        #self.robot = self.find('@')[0]

    def move(self, position, direction):
        if self.get(position + direction) == '.':
            self.set(position + direction, self.get(position))
            self.set(position, '.')
            return True
        elif self.get(position + direction) == '#':
            return False
        else:
            if self.move(position + direction, direction):
                return self.move(position, direction)
            else:
                return False

if __name__ == '__main__':
    chart = None
    moves = None

    with open(sys.argv[1]) as file:
        chart_lines = []
        chart_done = False
        moves = ""

        for line in file:
            if line.strip() and not chart_done:
                chart_lines.append(line)
            elif not line.strip():
                chart_done = True
            else:
                moves += line.strip()
        
        chart = BoxChart(chart_lines)

    #chart.print()
    #print("Moves: " + moves)

    for m in moves:
        chart.move(chart.find('@')[0], directions[m])
        #print("Move: " + m)
        #chart.print()
        #input("Space to continue...")

    chart.print()
    gps_total = 0
    for box in chart.find('O'):
        gps_total += box.x + (box.y * 100)
    print("GPS Total: ", gps_total)
