#!/usr/env/bin python3
import sys
import os
import re

sys.path.append(os.path.abspath('../'))
from coordinate import Coordinate

class ClawMachine:
    def __init__(self, machine_strings):
        self.button_offsets = {}
        self.prize = None

        self.parse_machine(machine_strings)

    def parse_machine(self, machine_strings):
        for mach_str in machine_strings:
            if mach_str.startswith('B'):
                self.button_offsets.update(self.parse_button(mach_str))
            elif mach_str.startswith('P'):
                self.prize = self.parse_prize(mach_str)                

    def parse_button(self, button_str):
        button_parsed = re.match(r'Button (\w): X\+(\d+), Y\+(\d+)', button_str)
        return { button_parsed.group(1): Coordinate(int(button_parsed.group(2)), int(button_parsed.group(3))) }
    
    def parse_prize(self, prize_str):
        prize_parsed = re.match(r'Prize: X=(\d+), Y=(\d+)', prize_str)
        return Coordinate(int(prize_parsed.group(1)), int(prize_parsed.group(2)))

    def solve_equation(self, a_offs, b_offs, p):
        solutions = []

        for a in range(int(p/a_offs) + 1):
            for b in range(int(p/b_offs) + 1):
                equation = a*a_offs + b*b_offs

                if equation == p:
                    solutions.append((a,b))
                elif equation >= p:
                    break
        
        return solutions

    def solve(self):
        print("wat.")
        solutions_x = self.solve_equation(self.button_offsets['A'].x, self.button_offsets['B'].x, self.prize.x)
        solutions_y = self.solve_equation(self.button_offsets['A'].y, self.button_offsets['B'].y, self.prize.y)

        possible_solutions = [solution for solution in solutions_x if solution in solutions_y]
        
        print(possible_solutions)

        return possible_solutions

    def cheapest_win_cost(self, a_cost, b_cost):
        solutions = self.solve()
        cost = [s[0] * a_cost + s[1] * b_cost for s in solutions]
        
        if cost:
            return min(cost)
        else:
            return None
        
    def print(self):
        print("A Offset: " + str(self.button_offsets['A']))
        print("B Offset: " + str(self.button_offsets['B']))
        print("Prize: " + str(self.prize))

if __name__ == '__main__':
    claw_machines = []

    with open(sys.argv[1]) as file:
        machine = []
        for line in file:
            stripped = line.strip()
            if stripped:
                machine.append(stripped)
            else:
                claw_machines.append(ClawMachine(machine))
                machine.clear()

        if machine:
            claw_machines.append(ClawMachine(machine))
            machine.clear()

    total_cost = 0
    for cm in claw_machines:
        cw = cm.cheapest_win_cost(3,1)
        if cw:
            total_cost += cw

    print("Total Cost: " + str(total_cost))
