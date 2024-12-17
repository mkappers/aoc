#!/usr/env/bin python3
import sys
import os

sys.path.append(os.path.abspath('../'))
from coordinate import Coordinate
from chart import Chart

directions = {'^': Coordinate(0,-1), '>': Coordinate(1,0), 'v': Coordinate(0,1), '<': Coordinate(-1,0)}

class BoxChart(Chart):
    def __init__(self, lines):
        wide_lines = []
        for line in lines:
            wide_line = ""
            for symbol in line:
                if symbol == '#':
                    wide_line += '##'
                elif symbol == 'O':
                    wide_line += '[]'
                elif symbol == '.':
                    wide_line += '..'
                elif symbol == '@':
                    wide_line += '@.'

            wide_lines.append(wide_line)

        super().__init__(wide_lines)

    def move_horizontal(self, position, direction):
        if self.get(position + direction) == '.':
            self.set(position + direction, self.get(position))
            self.set(position, '.')
            return True
        elif self.get(position + direction) == '#':
            return False
        else:
            if self.move_horizontal(position + direction, direction):
                return self.move_horizontal(position, direction)
            else:
                return False

    def vertical_check(self, positions, direction):
        # Return True if vertical movement possible
        # New Symbols
        ns = [self.get(pos) for pos in [pos + direction for pos in positions]]

        if all(s == '.' for s in ns):
            return True
        elif any(s == '#' for s in ns):
            return False

        if len(positions) == 1:
            # Robot Moving
            if ns[0] == ']':
                return self.vertical_check([(positions[0] + directions['<']) + direction, positions[0] + direction], direction)
            elif ns[0] == '[':
                return self.vertical_check([positions[0] + direction, (positions[0] + directions['>']) + direction], direction)

        else:
            # Box Moving
            if ''.join(ns) == '[]':
                return self.vertical_check([pos + direction for pos in positions], direction)
            elif ''.join(ns) == '].':
                return self.vertical_check([(positions[0] + directions['<']) + direction, positions[0] + direction], direction)
            elif ''.join(ns) == '.[':
                return self.vertical_check([positions[1] + direction, (positions[1] + directions['>']) + direction], direction)
            else:
                # ns is ']['
                return self.vertical_check([(positions[0] + directions['<']) + direction, positions[0] + direction], direction) and \
                   self.vertical_check([positions[1] + direction, (positions[1] + directions['>']) + direction], direction)

    # Move vertical for robot or box, so max 2 positions
    def move_vertical(self, positions, direction):
        # New Symbols
        ns = [self.get(pos) for pos in [pos + direction for pos in positions]]

        if all(s == '.' for s in ns):
            for p in positions:
                self.set(p + direction, self.get(p))
                self.set(p, '.')
            return True
        elif any(s == '#' for s in ns):
            return False

        if len(positions) == 1:
            # Robot Moving
            if ns[0] == ']':
                if self.move_vertical([(positions[0] + directions['<']) + direction, positions[0] + direction], direction):
                    return self.move_vertical(positions, direction)
                else:
                    return False
            elif ns[0] == '[':
                if self.move_vertical([positions[0] + direction, (positions[0] + directions['>']) + direction], direction):
                    return self.move_vertical(positions, direction)
                else:
                    return False

        else:
            # Box Moving
            if ''.join(ns) == '[]':
                if self.move_vertical([pos + direction for pos in positions], direction):
                    return self.move_vertical(positions, direction)
                else:
                    return False
            elif ''.join(ns) == '].':
                if self.move_vertical([(positions[0] + directions['<']) + direction, positions[0] + direction], direction):
                    return self.move_vertical(positions, direction)
                else:
                    return False
            elif ''.join(ns) == '.[':
                if self.move_vertical([positions[1] + direction, (positions[1] + directions['>']) + direction], direction):
                    return self.move_vertical(positions, direction)
                else:
                    return False
            else:
                # ns is ']['
                if self.move_vertical([(positions[0] + directions['<']) + direction, positions[0] + direction], direction) and \
                   self.move_vertical([positions[1] + direction, (positions[1] + directions['>']) + direction], direction):
                    return self.move_vertical(positions, direction)
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

    chart.print()
    user_input = input("Direction? ")

    while user_input:
        m = None
        if user_input[0] == 'h':
            m = '<'
        elif user_input[0] == 'l':
            m = '>'
        elif user_input[0] == 'k':
            m = '^'
        elif user_input[0] == 'j':
            m = 'v'

        if m in '<>':
            chart.move_horizontal(chart.find('@')[0], directions[m])
            chart.print()
        elif m in '^v':
            robot = chart.find('@')
            if chart.vertical_check(robot, directions[m]):
                chart.move_vertical(chart.find('@'), directions[m])
            chart.print()

        user_input = input("Direction? ")

    chart.print()
    gps_total = 0
    for box in chart.find('['):
        gps_total += box.x + (box.y * 100)
    print("GPS Total: ", gps_total)
