#!/usr/bin/env python3
import sys
import re

rules = {}
updates = []
output = 0

with open(sys.argv[1]) as file:
    for line in file:
        if '|' in line:
            rule = re.split(r'\|', line.strip())
            if rule[0] in rules:
                rules[rule[0]].append(rule[1])
            else:
                rules[rule[0]] = [rule[1]]

        elif line.strip():
            updates.append(re.split(r',', line.strip()))

#print("Rules:")
#print(rules)
#print()
#print("Updates:")
#print(updates)

# Print Check
incorrect_updates = []

for update in updates:
    update_correct = True
    for i in range(len(update)):
        if update[i] in rules:
            for page in update[:i]:
                if page in rules[update[i]]:
                    update_correct = False
                    break

        if not update_correct:
            break

    if update_correct:
        output += int(update[int(len(update)/2)])
    else:
        incorrect_updates.append(update)

print(output)
