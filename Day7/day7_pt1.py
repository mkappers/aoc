#!/usr/bin/env python3
import sys
import re
import operator

ops = {"+": operator.add, "*": operator.mul}

def find_calibration(result, value, operators, operands):
    #print("find_calibration("+str(result)+","+str(value)+","+str(operators)+","+str(operands)+")")
    if not operands:
        return result == value
    else:
        for op in operators:
            subtree = find_calibration(result, ops[op](value,operands[0]),operators,operands[1:])
            if subtree:
                return True
        return False

def main():
    calibrations = {}
    with open(sys.argv[1]) as file:
        for line in file:
            split = re.split(r':\s+', line.strip())
            calibrations[int(split[0])] = [int(num) for num in re.split(r'\s+', split[1])]

    #print(calibrations)

    calibration_result = 0
    for calibration in calibrations:
        if find_calibration(calibration,calibrations[calibration][0],["+","*"],calibrations[calibration][1:]):
            calibration_result += calibration

    print(calibration_result)

if __name__ == '__main__':
    main()
