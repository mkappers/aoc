from coordinate import Coordinate

class Chart:
    cardinal = [Coordinate(0,-1), Coordinate(1,0), Coordinate(0,1), Coordinate(-1,0)]

    def __init__(self, lines):
        self.map = []
        self.width = None
        self.height = None

        for line in lines:
            row = []
            for symbol in line.strip():
                row.append(symbol)
            
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

    def find(self, symbol):
        symbol_coordinates = []

        for x in range(self.width):
            for y in range(self.height):
                if self.get(Coordinate(x,y)) == symbol:
                    symbol_coordinates.append(Coordinate(x,y))

        return symbol_coordinates

    def get_valid_neighbours(self, coord):
        neighbours = []
        for d in Chart.cardinal:
            nb = coord + d
            if 0 <= nb.x < self.width and 0 <= nb.y < self.height:
                neighbours.append(nb)

        return neighbours

    def print(self):
        for row in self.map:
            print(''.join([str(th) for th in row]))
