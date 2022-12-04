'''
    This camp cleanup assignment checker computes information about duplicate cleanup assignments

    Run with 'python camp_cleanup_assignments.py <inputfile>'

    Written for python 3.8
'''

import sys
import re


def isIsAssignmentRangeContained(line: str) -> bool:
    match = re.search("(\d*)-(\d*),(\d*)-(\d*)", line)

    if not match:
        print(f"Error, invalid line format: {line}.")
        return False

    begin1 = int(match.group(1))
    end1 = int(match.group(2))
    begin2 = int(match.group(3))
    end2 = int(match.group(4))

    return (
        (begin1 <= begin2 and end1 >= end2)
        or (begin2 <= begin1 and end2 >= end1))


def isIsAssignmentRangeOverlap(line: str) -> bool:
    match = re.search("(\d*)-(\d*),(\d*)-(\d*)", line)

    if not match:
        print(f"Error, invalid line format: {line}.")
        return False

    begin1 = int(match.group(1))
    end1 = int(match.group(2))
    begin2 = int(match.group(3))
    end2 = int(match.group(4))

    return not (end1 < begin2 or end2 < begin1)


def main(args: list):
    if len(args) != 1:
        print(f"Error: wrong number of arguments. Got {len(args)}, Exected 1.")
        print(f"\tRun with 'python camp_cleanup_assignments.py <inputfile>'")
        return

    try:
        file = open(args[0], 'r')
    except FileNotFoundError:
        print(f"{args[0]} does not exist")
        return 0

    num_contained = 0
    num_overlap = 0
    for line in file:
        if isIsAssignmentRangeContained(line):
            num_contained += 1
        if isIsAssignmentRangeOverlap(line):
            num_overlap += 1

    print(f"Advent of code answer part 1: {num_contained}")
    print(f"Advent of code answer part 2: {num_overlap}")


if __name__ == '__main__':
    main(sys.argv[1:])
