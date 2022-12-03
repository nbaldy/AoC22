'''
    This rucksack calculator computes information about reorganizing the rucksack,

    Run with 'python rucksack_reorganization.py <inputfile>'

    Written for python 3.8
'''

import sys
from enum import Enum
import re

class ItemLocation(Enum):
    EMPTY = 0
    COMPARTMENT_1 = 1
    COMPARTMENT_2 = 2

class Rucksack():
    def __init__(self):
        self.items = [ItemLocation.EMPTY] * 52
    
    # Returns false if item already exists in the other component
    def addItem(self, item : int, location : ItemLocation) -> bool:
        if item < 1 or item > 52:
            print(f"Error: invalid item {item}; should be from 1-52")
            return False

        if ItemLocation.EMPTY != self.items[item - 1]:
            return location == self.items[item - 1]
        
        self.items[item - 1] = location
        return True
    
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
        
        if not rucksack.addItem(item_c1, ItemLocation.COMPARTMENT_1):
            return  item_c1

        if not rucksack.addItem(item_c2, ItemLocation.COMPARTMENT_2):
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
    

def main(args: list):
    if len(args) != 1:
        print(f"Error: wrong number of arguments. Got {len(args)}, Exected 1.")
        print(f"\tRun with 'python rucksack_reorganization.py <inputfile>'")
        return

    sum_duplicates = getDuplicateValueSum(args[0])
    print(f"Advent of code answer part 1: {sum_duplicates}")

if __name__ == '__main__':
    main(sys.argv[1:])
