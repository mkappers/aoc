#!/usr/env/bin python3
import sys

from coordinate import Coordinate

# North, East, South, West
cardinal = [Coordinate(0,-1),Coordinate(1,0),Coordinate(0,1),Coordinate(-1,0)]

class Region:
    def __init__(self, name, coordinates):
        self.name = name
        self.coordinates = set(coordinates)
        self.chart = self.create_region_chart()

    def __eq__(self, other):
        return self.name == other.name and self.coordinates == other.coordinates

    def create_region_chart(self):
        x_coords = [coordinate.x for coordinate in self.coordinates]
        y_coords = [coordinate.y for coordinate in self.coordinates]

        # Topleft is 0,0 generally
        tl = Coordinate(min(x_coords), min(y_coords))
        # Bottomright
        br = Coordinate(max(x_coords), max(y_coords))

        # Map width and height is +2 for the sides
        width = br.x - tl.x + 1 + 2
        height = br.y - tl.y + 1 + 2

        cd_correction = Coordinate(1,1) - tl
        chart = []
        for y in range(height):
            row = []
            for x in range(width):
                row.append('.')
            chart.append(row)

        for cd in self.coordinates:
            corrected = cd + cd_correction
            chart[corrected.y][corrected.x] = self.name

        return chart

    def calc_perimeter(self):
        perimeter = 0

        for rc in self.coordinates:
            for d in cardinal:
                if rc+d not in self.coordinates:
                    perimeter += 1

        return perimeter

    def calc_area(self):
        return(len(self.coordinates))
            
    def print(self):
        for row in self.chart:
            print(''.join([str(th) for th in row]))


class RegionMap:
    def __init__(self,filepath):
        self.map = []
        self.width = None
        self.height = None

        with open(filepath) as file:
            self.map = []
            for line in file:
                row = []
                for region in line.strip():
                    row.append(region)
                
                self.map.append(row)

        self.width = len(self.map[0])
        self.height = len(self.map)
    
    def get(self, coordinate):
        if 0 <= coordinate.x < self.width and 0 <= coordinate.y < self.height:
            return self.map[coordinate.y][coordinate.x]
        else:
            return IndexError
    
    def set(self, coordinate, symbol):
        if 0 <= coordinate.x < self.width and 0 <= coordinate.y < self.height:
            self.map[coordinate.y][coordinate.x] = symbol
        else:
            return IndexError

    def get_valid_neighbours(self, coord):
        neighbours = []
        for d in cardinal:
            nb = coord + d
            if 0 <= nb.x < self.width and 0 <= nb.y < self.height:
                neighbours.append(nb)

        return neighbours

    def get_region(self, coord):
        name = self.get(coord)
        region = [coord]
        checked = []

        checking = list(region)
        for coord in region:
            checking.extend(self.get_valid_neighbours(coord))

        cd_to_check = list(set(checking) - set(region) - set(checked))

        while cd_to_check:
            for cd in cd_to_check:
                if self.get(cd) == name:
                    region.append(cd)
                else:
                    checked.append(cd)
            
            # Checking loop
            checking = list(region)
            for coord in region:
                checking.extend(self.get_valid_neighbours(coord))

            cd_to_check = list(set(checking) - set(region) - set(checked))

        return Region(name, region)

    def set_region(self, symbol, region):
        for cd in region.coordinates:
            try:
                self.set(cd, symbol)
            except:
                pass

    def print(self):
        for row in self.map:
            print(''.join([str(th) for th in row]))

if __name__ == '__main__':
    rm_original = RegionMap(sys.argv[1])
    rm_strip = RegionMap(sys.argv[1])

    regions = []
    for y in range(rm_strip.height):
        for x in range(rm_strip.width):
            cd = Coordinate(x,y)
            if rm_strip.get(cd) != '.':
                region = rm_strip.get_region(cd)
                rm_strip.set_region('.',region)
                regions.append(region)

    total = 0  
    for r in regions:
        print("Region: " + r.name)
        r.print()
        rp = r.calc_perimeter()
        ra = r.calc_area()
        price = rp * ra
        total += price
        print("Perimeter: " + str(rp) + ", Area: " + str(ra) + ", Price: " + str(price))

    print("Total: " + str(total))
