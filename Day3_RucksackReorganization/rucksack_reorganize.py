'''
    This rucksack calculator computes information about reorganizing the rucksack,

    Run with 'python rucksack_reorganization.py <inputfile>'

    Written for python 3.8
'''

import sys
from enum import Enum
import re

class Compartments(Enum):
    EMPTY = 0
    COMPARTMENT_1 = 1
    COMPARTMENT_2 = 2

class Rucksack():
    def __init__(self):
        self.items = [Compartments.EMPTY.value] * 52

    # Returns false if item already exists in the other component
    def addItemToCompartment(self, item : int, location : Compartments) -> bool:
        if item < 1 or item > 52:
            print(f"Error: invalid item {item}; should be from 1-52")
            return False

        if Compartments.EMPTY != Compartments(self.items[item - 1]):
            return location == self.items[item - 1]

        self.items[item - 1] = location
        return True

    # Maps the rucksack to a mask setup where rucksack 0 is binary 0, etc
    # Keeps track of which sack has which item
    def addItemToGroup(self, item : int, rucksack_num: int) -> int:
        if item < 1 or item > 52:
            print(f"Error: invalid item {item}; should be from 1-52")
            return False

        self.items[item - 1] |= 1 << rucksack_num

        return self.items[item - 1]

    def __str__(self):
        return str(self.items)

# Computes the priority of a single character
def getItemPriority(item : str) -> int:
    if ord('a') <= ord(item) and ord(item) <= ord('z'):
        return ord(item) - ord('a') + 1 # Lowercase starts at 1
    if ord('A') <= ord(item) and ord(item) <= ord('Z'):
        return ord(item) - ord('A') + 27 # Uppercase starts at 27

    print(f"ERROR: invalid line item {item}")
    return 0

def findDuplicateRucksackItem(line: str) -> int:
    line = line.strip()

    if len(line) % 2 != 0:
        print(f"Error, not even number of items: {line}, length is {len(line)}")
        return 0

    rucksack = Rucksack()
    for i in range(len(line)//2):
        item_c1 = getItemPriority(line[i])
        item_c2 = getItemPriority(line[-1-i])

        if not rucksack.addItemToCompartment(item_c1, Compartments.COMPARTMENT_1):
            return  item_c1

        if not rucksack.addItemToCompartment(item_c2, Compartments.COMPARTMENT_2):
            return  item_c2

    print(f"\nNo duplicates found: {rucksack}")
    return 0

def getDuplicateValueSum(filename : str) -> int:
    try:
        file = open(filename, 'r')
    except FileNotFoundError:
        print(f"{filename} does not exist")
        return 0

    sum_duplicates = 0
    for line in file:
        sum_duplicates += findDuplicateRucksackItem(line)

    return sum_duplicates

def getBadgeValueSum(filename : str) -> int:
    try:
        file = open(filename, 'r')
    except FileNotFoundError:
        print(f"{filename} does not exist")
        return 0

    sum_badges = 0

    while True:
        group_rucksacks = Rucksack()

        # First elf
        elf1_line = file.readline().strip()
        elf2_line = file.readline().strip()
        elf3_line = file.readline().strip()
        if not elf1_line:
            # Done processing - assume sets of 3 but if not process as if remainders are empty
            break

        # Technically if we *really* cared, we should probably process the sacks round-robin style
        # As this reduces our omega bound (because theoretically if all of the first elements are duplicates,
        # the check occurs in constant time (check the first element of each elf) rather than linear time
        for item in elf1_line:
            # Don't care about result - not enough info yet
            _ = group_rucksacks.addItemToGroup(getItemPriority(item), 0)
        for item in elf2_line:
            # Don't care about result - not enough info yet
            _ = group_rucksacks.addItemToGroup(getItemPriority(item), 1)
        for item in elf3_line:
            item_val = getItemPriority(item)
            item_compartments = group_rucksacks.addItemToGroup(item_val, 2)
            if  0b111 == item_compartments:
                # Present in all 3 compartments
                sum_badges += item_val
                break

    return sum_badges



def main(args: list):
    if len(args) != 1:
        print(f"Error: wrong number of arguments. Got {len(args)}, Exected 1.")
        print(f"\tRun with 'python rucksack_reorganization.py <inputfile>'")
        return

    sum_duplicates = getDuplicateValueSum(args[0])
    print(f"Advent of code answer part 1: {getDuplicateValueSum(args[0])}")
    print(f"Advent of code answer part 2: {getBadgeValueSum(args[0])}")

if __name__ == '__main__':
    main(sys.argv[1:])
