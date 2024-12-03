#!/usr/bin/env python3
import sys
import re

corrupted_memory = []
with open(sys.argv[1]) as file:
    for line in file:
        corrupted_memory.append(line.strip())

program_output = 0
for mem_block in corrupted_memory:
    valid_instructions = re.findall(r'mul\(\d{1,3}\,\d{1,3}\)', mem_block)
    
    for instruction in valid_instructions:
        inst_params = re.match(r'mul\((\d{1,3})\,(\d{1,3})\)', instruction)
        inst_result = int(inst_params.group(1)) * int(inst_params.group(2))
        program_output += inst_result

print(program_output)
