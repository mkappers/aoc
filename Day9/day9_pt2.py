#!/usr/env/bin python3
import sys

class DiskMap:
    def __init__(self, diskmap):
        self.diskmap = diskmap
        self.disklayout = None
        self.files = None
        self.blocks = None

    def calc_layout(self):
        self.disklayout = []
        self.files = []
        for i in range(len(self.diskmap)):
            if i % 2 == 0:
                if self.diskmap[i] != '0':
                    self.files.append(str(int(i/2)))
                self.disklayout.extend([str(int(i/2))] * int(self.diskmap[i]))
            else:
                self.disklayout.extend(['.'] * int(self.diskmap[i]))

    def find_file_block(self, file_id):
        # Left bound inclusive, right bound exclusive
        lb = None
        rb = None
        for i in range(len(self.disklayout)):
            if self.disklayout[i] == file_id and lb is None:
                lb = i
            elif self.disklayout[i] != file_id and lb is not None:
                rb = i

            if lb is not None and rb is not None:
                break

        # End of list
        if lb is not None and rb is None:
            rb = len(self.disklayout)

        return (lb, rb)

    def find_free_block(self, size, layout):
        # Left bound inclusive, right bound exclusive
        lb = None
        rb = None
        for i in range(len(layout)):
            if layout[i] == '.' and lb is None:
                lb = i
            elif layout[i] != '.' and lb is not None:
                rb = i

            if lb is not None and rb is not None:
                if rb - lb >= size:
                    break
                else:
                    lb = None
                    rb = None

        # End of list
        if lb is not None and rb is None:
            if len(layout) - lb >= size:
                rb = len(layout)
            else:
                return None
        elif lb is None and rb is None:
            return None

        return (lb, rb)

    def switch_blocks(self, a, b):
        self.disklayout = self.disklayout[:a[0]] + self.disklayout[b[0]:b[1]] + self.disklayout[a[1]:b[0]] + self.disklayout[a[0]:a[1]] + self.disklayout[b[1]:len(self.disklayout)]

    def compact(self):
        if self.disklayout is None:
            self.calc_layout()

        for file in reversed(self.files):
            # Find file bounds and fitting free bounds
            file_bounds = self.find_file_block(file)
            file_size = file_bounds[1] - file_bounds[0]
            
            free_bounds = self.find_free_block(file_size, self.disklayout[:file_bounds[0]])
            
            if free_bounds is not None:
                self.switch_blocks((free_bounds[0], free_bounds[0]+file_size),file_bounds)

    def checksum(self):
        cs = 0
        for i in range(len(self.disklayout)):
            if self.disklayout[i] == '.':
                continue
            cs += i * int(self.disklayout[i])

        return cs

    def __str__(self):
        return "Diskmap: " + str(self.diskmap) + "\nLayout:  " + str(''.join(self.disklayout)) + "\nFiles: " + str(self.files)

if __name__ == "__main__":
    puzzle_input = None

    with open(sys.argv[1]) as file:
        for line in file:
            puzzle_input = line.strip()
            break

    dm = DiskMap(puzzle_input)
    dm.compact()
    #print(dm)


    print("Checksum:", dm.checksum())
