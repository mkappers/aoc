#!/usr/bin/env python3
import sys
import re

corrupted_memory = "" 
with open(sys.argv[1]) as file:
    for line in file:
        corrupted_memory += line.strip()

program_output = 0

# Program is single line
dont_blocks = re.split(r'don\'t\(\)', corrupted_memory)

enabled_blocks = [dont_blocks[0]]

for dont_block in dont_blocks:
    print("Dont Block: " + dont_block + "\n")
    do_blocks = re.split(r'do\(\)', dont_block)
    enabled_blocks += do_blocks[1:]
    print("Do Blocks Slice: ")
    print(do_blocks[1:])
    print("\n")


print("Enabled Blocks" + str(len(enabled_blocks)) + ": ")
print(enabled_blocks)
print("\n")

for enabled_block in enabled_blocks:
    valid_instructions = re.findall(r'mul\(\d{1,3}\,\d{1,3}\)', enabled_block)
    print(valid_instructions)
    for instruction in valid_instructions:
        inst_params = re.match(r'mul\((\d{1,3})\,(\d{1,3})\)', instruction)
        inst_result = int(inst_params.group(1)) * int(inst_params.group(2))
        program_output += inst_result

print(program_output)
