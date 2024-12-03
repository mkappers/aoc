#!/usr/bin/env python3
import sys
import re

def report_safe(report):
    inc = None
    
    # Initial Movement
    change = report[1] - report[0]
    if abs(change) >= 1 and abs(change) <= 3:
        inc = True if change > 0 else False
    else:
        return False
   
    for stop in range(2, len(report)):
        change = report[stop] - report[stop - 1]
        if (abs(change) < 1 or abs(change) > 3) or ((change > 0) != inc):
            return False
    
    return True

reports = []
with open(sys.argv[1]) as file:
    for line in file:
        levels = []
        for level in re.split('\s+', line.strip()):
            levels.append(int(level))
        reports.append(levels)


safe = 0
dampen = []

# Initial Run
for report in reports:
    if report_safe(report):
        safe += 1
    else:
        dampen.append(report)

print("Safe without dampen: " + str(safe))

# Dampened Run
for report in dampen:
    for i in range(len(report)):
        dampened = report.copy()
        del dampened[i]
        if report_safe(dampened):
            safe += 1
            break

print("Safe with dampen: " + str(safe))
