#!/usr/env/bin python3
import sys
import string

class Coordinate:
    # Coordinate Class
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Coordinate(self.x * other, self.y * other)

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
    
    def __repr__(self):
        return "Coordinate(" + str(self.x) + "," + str(self.y) + ")"

class Map:
    # Map Class
    def __init__(self):
        self.map = []
        self.width = None
        self.height = None

    def __init__(self,width=0,height=0):
        self.map = []
        self.width = width
        self.height = height

        for h in range(height):
            row = []
            for w in range(width):
                row.append('.')
            self.map.append(row)
    
    def import_map(self,filepath):
        with open(filepath) as file:
            self.map = []
            for line in file:
                row = []
                for position in line.strip():
                    row.append(position)
        
                self.map.append(row)

        self.width = len(self.map[0])
        self.height = len(self.map)
    
    def get(self,coordinate):
        return self.map[coordinate.y][coordinate.x]

    def set(self,coordinate,symbol):
        if 0 > coordinate.x or 0 > coordinate.y:
            raise IndexError('coordinates out of map range')
        self.map[coordinate.y][coordinate.x] = symbol

    def find(self,symbol):
        coordinate_list = []

        for x in range(self.width):
            for y in range(self.height):
                coord = Coordinate(x,y)
                if self.get(coord) == symbol:
                    coordinate_list.append(coord)

        return coordinate_list

    def print(self):
        print("Print")
        for row in self.map:
            print(''.join(row))

if __name__ == '__main__':
    antinode_total = 0

    puzzle_map = Map()
    puzzle_map.import_map(sys.argv[1])
    antinode_map = Map(puzzle_map.width,puzzle_map.height)

    frequency_symbols = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)
    frequency_dict = {}

    for symbol in frequency_symbols:
        symbol_positions = puzzle_map.find(symbol)
        if symbol_positions:
            frequency_dict[symbol] = symbol_positions

    for freq in frequency_dict:
        for i in range(len(frequency_dict[freq])):
            ca = frequency_dict[freq][i]
            oa = frequency_dict[freq][:i] + frequency_dict[freq][i+1:]

            for a in oa:
                distance = a - ca

                # Draw Antinode
                try:
                    antinode_map.set(a + distance, '#')
                except:
                    pass

                antinode_total += 1

    antinode_map.print()
    
    print("Total Antinodes:", antinode_total)
    print("In-Bound Antinodes:", len(antinode_map.find('#')))
