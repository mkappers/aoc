#!/usr/bin/env python3
import sys
import re

corrupted_memory = "" 
with open(sys.argv[1]) as file:
    for line in file:
        corrupted_memory += line.strip()

program_output = 0

# Program is single line
valid_instructions = re.findall(r'(?:mul\(\d{1,3}\,\d{1,3}\))|(?:don\'t\(\))|(?:do\(\))', corrupted_memory)
#print(valid_instructions)

enabled = True
program_output = 0
for instruction in valid_instructions:
    if instruction[0] == 'm' and enabled:
        inst_params = re.match(r'mul\((\d{1,3})\,(\d{1,3})\)', instruction)
        inst_result = int(inst_params.group(1)) * int(inst_params.group(2))
        program_output += inst_result
    elif instruction[2] == 'n':
        enabled = False
    elif instruction[2] == '(':
        enabled = True

print(program_output)
