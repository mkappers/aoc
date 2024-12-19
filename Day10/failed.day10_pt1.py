#!/usr/env/bin python3
import sys
import string

# Based on Day 8
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

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y
    
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
    
    def __repr__(self):
        return "Coordinate(" + str(self.x) + "," + str(self.y) + ")"

class Trail:
    def __init__(self,trailhead,trail,peak):
        self.trailhead = trailhead
        self.trail = trail
        self.peak = peak

class TopographicMap:
    directions = [
        Coordinate(0,-1),  #"north"
        Coordinate(1,0),   #"east" 
        Coordinate(0,1),   #"south"
        Coordinate(-1,0)   #"west" 
    ]

    def __init__(self,filepath):
        self.map = []
        self.width = None
        self.height = None
        self.trailheads = []

        with open(filepath) as file:
            self.map = []
            y = 0
            for line in file:
                x = 0
                row = []
                for topo_height in line.strip():
                    row.append(int(topo_height))
                    if int(topo_height) == 0:
                        self.trailheads.append(Coordinate(x,y))
                    x += 1
        
                self.map.append(row)
                y += 1

        self.width = len(self.map[0])
        self.height = len(self.map)
    
    def get(self,coordinate):
        if 0 <= coordinate.x < self.width and 0 <= coordinate.y < self.height:
            return self.map[coordinate.y][coordinate.x]
        else:
            return IndexError

    def print(self):
        for row in self.map:
            print(''.join([str(th) for th in row]))

    def traverse_trail(self, trails, path, nextpos):
        print("Traverse: ", str(path), str(nextpos))
        origin = None
        origin_value = None
        nextpos_value = None
        try:
            nextpos_value = self.get(nextpos)
        except:
            return

        print(path)
        if len(path) > 0:
            origin = path[-1] - nextpos
            origin_value = self.get(path[-1])
            
            if nextpos_value - origin_value == 1:
                new_path = path[:]
                new_path.append(nextpos)
                if nextpos_value == 9:
                    trails.append(Trail(path[0], new_path, nextpos))
                else:
                    for d in [cd for cd in TopographicMap.directions if cd != origin]:
                        self.traverse_trail(trails, new_path, nextpos + d)
        else:
            print(TopographicMap.directions)
            for d in TopographicMap.directions:
                print(d)
                self.traverse_trail(trails, [nextpos], nextpos + d)


    def find_trails(self):
        trails = []
        for th in self.trailheads:
            self.traverse_trail(trails,[],th)

        return trails

if __name__ == '__main__':
    # Import Topographic Map 
    tm = TopographicMap(sys.argv[1])

    print(tm.trailheads)
    trails = []
    tm.traverse_trail(trails,[],tm.trailheads[0])
    
    # Traverse
    #trails_result = tm.find_trails()

    tm.print()
    print(trails)
    print(len(trails))
