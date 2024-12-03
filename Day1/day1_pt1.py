#!/usr/bin/env python3
import sys
import re

l_list = []
r_list = []
with open(sys.argv[1]) as file:
    for line in file:
        numbers = re.split('\s+', line)
        l_list.append(int(numbers[0]))
        r_list.append(int(numbers[1]))

l_list.sort()
r_list.sort()

result = 0
for i in range(len(l_list)):
    result += abs(l_list[i] - r_list[i])

print(result)
