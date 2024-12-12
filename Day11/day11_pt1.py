#!/usr/env/bin python3
import sys
import re

class Stone:
    def __init__(self, value = None, parent = None):
        self.parent = parent
        self.children = []
        
        if value is not None:
            self.value = int(value)
            self.engraving = str(self.value)
    
    def blink(self, num_blinks):
        if num_blinks > 0:
            self.children = self.apply_rules()

            for stone in self.children:
                stone.blink(num_blinks - 1)
        else:
            return

    def apply_rules(self):
        # Returns a list of stones
        if self.value == 0:
            return [Stone('1', self)]
        if len(self.engraving) % 2 == 0:
            return [Stone(self.engraving[:int(len(self.engraving)/2)],self),Stone(self.engraving[int(len(self.engraving)/2):])]
        else:
            return [Stone(str(self.value * 2024), self)]
    
    def count_level(self, level):
        if level <= 0:
            return 1
        else:
            count = 0
            for stone_child in self.children:
                count += stone_child.count_level(level - 1)
            return count

    def __repr__(self):
        return "Stone(" + self.engraving + ")"
            
if __name__ == "__main__":
    root = Stone()

    with open(sys.argv[1]) as file:
        for line in file:
            engravings = re.split('\s+', line.strip())
            for engraving in engravings:
                root.children.append(Stone(engraving))

    blinks = int(sys.argv[2])
    for stone in root.children:
        stone.blink(blinks)

    print("Number of magic stones: " + str(root.count_level(blinks + 1)))
