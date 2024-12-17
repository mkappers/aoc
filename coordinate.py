import math

class Coordinate:
    # Coordinate Class
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def normalize(self):
        self.x = self.x / self.magnitude()
        self.y = self.y / self.magnitude()

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

    def __hash__(self):
        return hash(str(self))
    
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
    
    def __repr__(self):
        return "Coordinate(" + str(self.x) + "," + str(self.y) + ")"
