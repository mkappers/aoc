#!/usr/bin/env python3
import sys
import re

reports = []
with open(sys.argv[1]) as file:
    for line in file:
        levels = []
        for level in re.split('\s+', line.strip()):
            levels.append(int(level))
        reports.append(levels)

safe = 0
for report in reports:
    inc = None
    
    # Initial Movement
    change = report[1] - report[0]
    if abs(change) >= 1 and abs(change) <= 3:
        inc = True if change > 0 else False
    else:
        continue
   
    #
    unsafe = False
    for stop in range(2, len(report)):
        change = report[stop] - report[stop - 1]
        if (abs(change) < 1 or abs(change) > 3) or ((change > 0) != inc):
            unsafe = True
            break
    if unsafe == False:
        safe += 1

print(safe)
