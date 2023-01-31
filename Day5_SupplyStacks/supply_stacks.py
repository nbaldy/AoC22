'''
    This camp cleanup assignment checker computes information about duplicate cleanup assignments

    Run with 'python supply_stacks.py <inputfile>'

    Written for python 3.8
'''

import sys
import re


def getNumElementsInStackLine(line: str) -> int:
    if len(line) % 4 != 0:
        print(f"Invalid number of elements in line, not divisible by 4: {line}")
        return -1
    return len(line) // 4

# Return true if line is successfully read. Ideally I would make an enum but I'm cranky from fighting with regex now
# Modifies stacks in-place
def readStackLine(line: str, stacks: list) -> bool:
    num_elems = getNumElementsInStackLine(line)
    if num_elems != len(stacks):
        print(f"Invalid line length: expected {len(stacks)} got {num_elems}")
        return False
    
    if line[(num_elems-1)*4:].strip().isnumeric():
        # This is the number line
        return False

    for row in range(num_elems):
        if line[row*4 + 1] != ' ':
            stacks[row].append(line[row*4 + 1])
    
    return True

# Return true if line is successfully read
# Modifies stacks in-place
def readMoveLineOneByOne(line: str, stacks: list)->bool:
    # move_line_regex =  "move (\d*) from (\d*) to (\d*)"
    match = re.search(move_line_regex, line)
    if not match:
        print(f"Invalid line: {line}")
        return False

    try:
        num_to_move, col_from, col_to = [int(group) for group in match.groups()]
    except ValueError:
        print(f"Invalid line, not numeric moves: {line}")
        return False

    if min(col_from, col_to) < 0 or max(col_from, col_to) > len(stacks):
        print(f"Invalid columns: {col_from}, {col_to}, there are {len(stacks)} columns")
        return False
    
    if num_to_move > len(stacks[col_from-1]):
        print(f"Invalid move: only {len(stacks[col_from-1])} items in column {col_from}")
        return False
    
    for n in range(num_to_move):
        stacks[col_to-1].append(stacks[col_from-1].pop())
    return True

def readMoveLineTogether(line: str, stacks: list)->bool:
    # move_line_regex =  "move (\d*) from (\d*) to (\d*)"
    match = re.search(move_line_regex, line)
    if not match:
        print(f"Invalid line: {line}")
        return False

    try:
        num_to_move, col_from, col_to = [int(group) for group in match.groups()]
    except ValueError:
        print(f"Invalid line, not numeric moves: {line}")
        return False

    if min(col_from, col_to) < 0 or max(col_from, col_to) > len(stacks):
        print(f"Invalid columns: {col_from}, {col_to}, there are {len(stacks)} columns")
        return False
    
    if num_to_move > len(stacks[col_from-1]):
        print(f"Invalid move: only {len(stacks[col_from-1])} items in column {col_from}")
        return False
    
    stacks[col_to-1] += stacks[col_from-1][-num_to_move:]
    del stacks[col_from-1][-num_to_move:]

    return True

def readFinalTopCrates(filename: str, moveParser)->str:
    try:
        file = open(filename, 'r')
    except FileNotFoundError:
        print(f"{filename} does not exist")
        return 0

    line = file.readline() # Don't strip here, whitespace matters
    stacks = []
    for row in range(len(line)//4):
        stacks.append([]) # Cannot be coppies of each other ([[]]*N)
    while readStackLine(line, stacks):
        line = file.readline()

    # Next line is an empty line
    file.readline()
    line = file.readline().strip()
    
    # We create the stacks in reverse so reverse them
    for stack in stacks:
        stack.reverse()
    print(stacks)
    while line:
        if not moveParser(line, stacks):
            print("Error moving stacks")
            return ""
        print(line, stacks)
        line = file.readline().strip()

    # Compute the top layer    
    return_str = ""
    for stack in stacks:
        return_str += stack[-1]

    return str([stack[-1] for stack in stacks])

def main(args: list):
    if len(args) != 1:
        print(f"Error: wrong number of arguments. Got {len(args)}, Exected 1.")
        print(f"\tRun with 'python supply_stacks.py <inputfile>'")
        return

    print(f"Advent of code answer part 1: {readFinalTopCrates(args[0], readMoveLineOneByOne)}")
    print(f"Advent of code answer part 2: {readFinalTopCrates(args[0], readMoveLineTogether)}")

if __name__ == '__main__':
    main(sys.argv[1:])
