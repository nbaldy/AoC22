'''
    This calculator computes the most calories carried by the elf,
    It reads from a simple file where each line is either a number of calories
    or is blank (indicating a new elf's entry begins on the following lines).
    It should output the number of calories carried by the elf with the most calories.

    Run with 'python max_calorie_calculator.py <inputfile>'

    Written for python 3.8
'''

# Needed for python 3.8
from typing import List
import heapq

class Elf:
    def __init__(self, num: int, calories: int):
        self.__num = num
        self.__calories = calories

    def addCalories(self, calories: int):
        self.__calories += calories

    def calories(self) -> int:
        return self.__calories

    def number_in_line(self) -> int:
        return self.__num

    # Enables heapq to sort properly
    def __lt__(self, other):
        return self.__calories < other.__calories

    def __gt__(self, other):
        return self.__calories > other.__calories

    def __eq__(self, other):
        return self.__calories == other.__calories

    # Return an empty elf with the next number
    def getNextElf(self):
        return Elf(self.__num + 1, 0)

# Returns the Elf carrying the most calories.
def getMostCarriedCalories(filename : str) -> Elf:
    mostElfList = getNMostCarriedCalories(filename, 1)
    if not mostElfList:
        print("Error getting most elf")
        return Elf(0, 0)

    return mostElfList[0]

# Returns the top N Elfs carrying the most calories.
def getNMostCarriedCalories(filename: str, N: int) -> List[Elf]:
    try:
        file = open(filename, 'r')
    except FileNotFoundError:
        print(f"{filename} does not exist")
        return []


    current_elf = Elf(0, 0)
    most_elves = [current_elf] * N

    for line in file:
        if not line or line == '\n':
            # Heappush pop handles rejecting the update if it is already in the heap
            heapq.heappushpop(most_elves, current_elf)
            current_elf = current_elf.getNextElf()
        else:
            current_elf.addCalories(int(line))

    file.close()
    return most_elves

def main(args : list):
    if len(args) != 1:
        print(f"Error: wrong number of arguments. Got {len(args)}, Exected 1.")
        print(f"\tRun with 'python max_calorie_calculator.py <inputfile>'")
        return

    elves_most_3 = getNMostCarriedCalories(args[0], 3)

    # Rather than computing the most, just get it from the group of 3 - heap does not guarentee biggest in last
    if len(elves_most_3) != 3:
        print ("Error getting the top 3 elves")
        return

    print(f"Elves with the most calories (first in line is Elf 0): ")
    max_cal = 0
    for elf in elves_most_3:
        # Technically we know the first one is the smallest, but
        print(f"\tElf {elf.number_in_line()}: {elf.calories()} calories.")
        max_cal += elf.calories()

    most_elf = max(elves_most_3[1:]) # We know the first element is the smallest
    print(f"Advent of code answer part 1: {most_elf.calories()}")
    print(f"Advent of code answer part 2: {max_cal}")

import sys
if __name__ == '__main__':
    main(sys.argv[1:])