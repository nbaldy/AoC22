'''
    This calculator computes the most calories carried by the elf,
    It reads from a simple file where each line is either a number of calories 
    or is blank (indicating a new elf's entry begins on the following lines).
    It should output the number of calories carried by the elf with the most calories.

    Run with 'python max_calorie_calculator.py <inputfile>'
'''

from typing import Tuple

# Returns the elf number (superfluous) and calories of the elf carrying the most. 
#   tuple(elf_number, elf_calories)
def getMostCarriedCalories(filename : str) -> Tuple[int, int]:
    try:
        file = open(filename, 'r')
    except FileNotFoundError:
        print(f"{filename} does not exist")
        return (0,0)

    current_elf_number = 0
    current_elf_calories = 0
    most_elf_number = 0
    most_elf_calories = 0
    for line in file:
        if not line or line == '\n':
            # New elf on next line
            if (current_elf_calories > most_elf_calories):
                most_elf_number = current_elf_number
                most_elf_calories = current_elf_calories
            
            current_elf_number += 1
            current_elf_calories = 0
        else:
            current_elf_calories += int(line)

    file.close()
    return (most_elf_number, most_elf_calories)

def main(args : list):
    if len(args) != 1:
        print(f"Error: wrong number of arguments. Got {len(args)}, Exected 1.")
        print(f"\tRun with 'python max_calorie_calculator.py <inputfile>'")
        return
    
    (elf_number, elf_calories) = getMostCarriedCalories(args[0])

    print(f"Elf {elf_number} was carrying the most calories: {elf_calories}")
    print(f"Advent of code answer: {elf_calories}") 

import sys
if __name__ == '__main__':
    main(sys.argv[1:])