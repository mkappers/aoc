#!/usr/env/bin python3
import sys

class DiskMap:
    def __init__(self, diskmap):
        self.diskmap = diskmap
        self.blocks = None

    def calc_blocks(self):
        self.blocks = []
        for i in range(len(self.diskmap)):
            if i % 2 == 0:
                self.blocks.extend([str(int(i/2))] * int(self.diskmap[i]))
            else:
                self.blocks.extend(['.'] * int(self.diskmap[i]))

    def compact(self):
        if self.blocks is None:
            self.calc_blocks()

        # Index Checks
        il = 0
        ir = len(self.blocks) - 1
        while il != ir and il < ir:
            if self.blocks[il] == '.' and self.blocks[ir] != '.':
                self.blocks[il] = self.blocks[ir]
                self.blocks[ir] = '.'
            while self.blocks[il] != '.':
                il += 1
            while self.blocks[ir] == '.':
                ir -= 1

    def checksum(self):
        cs = 0
        for i in range(len(self.blocks)):
            if self.blocks[i] == '.':
                break
            cs += i * int(self.blocks[i])

        return cs

    def __str__(self):
        return "Diskmap: " + str(self.diskmap) + "\nBlocks:  " + str(''.join(self.blocks))

if __name__ == "__main__":
    puzzle_input = None

    with open(sys.argv[1]) as file:
        for line in file:
            puzzle_input = line.strip()
            break

    dm = DiskMap(puzzle_input)
    #dm.calc_blocks()
    dm.compact()
    #print(dm)
    print("Checksum:", dm.checksum())
