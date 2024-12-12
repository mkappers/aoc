#!/usr/env/bin python3
import sys
import re

stones = []
blinkdict = {}

def update_dict(engraving, delta):
    if engraving in blinkdict:
        blinkdict[engraving] += delta
    else:
        blinkdict[engraving] = 1

def apply_rules(engraving):
    # Returns a list of stones
    if engraving == '0':
        update_dict('1', 1)
        update_dict('0', -1)
    if len(engraving) % 2 == 0:
        update_dict(str(int(engraving[:int(len(engraving)/2)])),1)
        update_dict(str(int(engraving[int(len(engraving)/2):])),1)
        update_dict(engraving,-1)
    else:
        update_dict(str(int(engraving) * 2024), 1)
        update_dict(engraving, -1)
            
if __name__ == "__main__":

    with open(sys.argv[1]) as file:
        for line in file:
            engravings = re.split('\s+', line.strip())
            for engraving in engravings:
                stones.append(engraving)

    blinks = int(sys.argv[2])

    for blink in range(blinks + 1):
        print(blink)
        if blink == 0:
            for engraving in engravings:
                update_dict(engraving, 1)
        else:
            dictcopy = dict(blinkdict)
            for key in dictcopy:
                for i in range(dictcopy[key]):
                    apply_rules(key)
        
        #print(blinkdict)

    count = 0
    for engraving in blinkdict:
        count += blinkdict[engraving]

    print("Number of magic stones: " + str(count))
