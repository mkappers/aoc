#!/usr/bin/env python3
import sys
import re

from collections import Counter

l_list = []
r_list = []
with open(sys.argv[1]) as file:
    for line in file:
        numbers = re.split('\s+', line)
        l_list.append(int(numbers[0]))
        r_list.append(int(numbers[1]))

appearances = Counter(r_list)

similarity = 0
for loc_id in l_list:
    similarity += loc_id * appearances[loc_id]

print(similarity)
