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

def update_correct(update):
    update_correct = True
    for i in range(len(update)):
        if update[i] in rules:
            for page in update[:i]:
                if page in rules[update[i]]:
                    update_correct = False
                    break

        if not update_correct:
            break

    return update_correct

def rectify_update(update):
    for i in range(len(update)):
        if update[i] in rules:
            for j in range(i):
                if update[j] in rules[update[i]]:
                    update.insert(i+1,update[j])
                    update.pop(j)


#print("Rules:")
#print(rules)
#print()
#print("Updates:")
#print(updates)

# Print Check
incorrect_updates = []

for update in updates:
    if not update_correct(update):
        incorrect_updates.append(update)

#print(incorrect_updates)

for update in incorrect_updates:
    while not update_correct(update):
        rectify_update(update)
    
    output += int(update[int(len(update)/2)])

print(output)
