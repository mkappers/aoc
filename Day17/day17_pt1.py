#!/usr/bin/env python3
import sys
import math

registers = {}
program = []
output = []
instruction_pointer = 0

def combo(operand):
    if 0 <= operand < 4:
        return operand
    elif operand == 4:
        return registers['A']
    elif operand == 5:
        return registers['B']
    elif operand == 6:
        return registers['C']
    else:
        raise ValueError

def adv(operand):
    global instruction_pointer
    registers['A'] = int(registers['A'] / pow(2, combo(operand)))
    instruction_pointer += 2

def bxl(operand):
    global instruction_pointer
    registers['B'] = registers['B'] ^ operand
    instruction_pointer += 2

def bst(operand):
    global instruction_pointer
    registers['B'] = combo(operand) % 8
    instruction_pointer += 2

def jnz(operand):
    global instruction_pointer
    if registers['A'] == 0:
        instruction_pointer += 2
    else:
        instruction_pointer = operand

def bxc(operand):
    global instruction_pointer
    registers['B'] = registers['B'] ^ registers['C']
    instruction_pointer += 2

def out(operand):
    global instruction_pointer
    output.append(str(combo(operand) % 8))
    instruction_pointer += 2

def bdv(operand):
    global instruction_pointer
    registers['B'] = int(registers['A'] / pow(2, combo(operand)))
    instruction_pointer += 2

def cdv(operand):
    global instruction_pointer
    registers['C'] = int(registers['A'] / pow(2, combo(operand)))
    instruction_pointer += 2

def run(opcode, operand):
    match opcode:
        case 0:
            adv(operand)
        case 1:
            bxl(operand)
        case 2:
            bst(operand)
        case 3:
            jnz(operand)
        case 4:
            bxc(operand)
        case 5:
            out(operand)
        case 6:
            bdv(operand)
        case 7:
            cdv(operand)

if __name__ == '__main__':

    with open(sys.argv[1]) as file:
        for line in file:
            stripped = line.strip()
            if stripped.startswith("Register"):
                split = stripped.split()
                registers[split[1][0]] = int(split[2])
            elif stripped.startswith("Program"):
                split = stripped.split()
                program = [int(p) for p in split[1].split(',')]

    print(registers)
    print(program)

    while instruction_pointer < len(program):
        run(program[instruction_pointer], program[instruction_pointer + 1])

    print(','.join(output))
