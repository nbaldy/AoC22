'''
    This strategy calculator computes the score of the Tic-tac-toe play,

    Run with 'python rock_paper_scissors.py <inputfile>'

    Written for python 3.8
'''

import sys
from enum import Enum
import re

class RockPaperScissors(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


class Result(Enum):
    LOSS = 0
    TIE = 3
    WIN = 6


def getElfPlay(file_val: str) -> RockPaperScissors:
    if file_val == "A":
        return RockPaperScissors.ROCK
    elif file_val == "B":
        return RockPaperScissors.PAPER
    elif file_val == "C":
        return RockPaperScissors.SCISSORS
    else:
        print(f"Invalid elf value: {file_val}.")
        return -1


def getYourPlay(file_val: str) -> RockPaperScissors:
    if file_val == "X":
        return RockPaperScissors.ROCK
    elif file_val == "Y":
        return RockPaperScissors.PAPER
    elif file_val == "Z":
        return RockPaperScissors.SCISSORS
    else:
        print(f"Invalid elf value: {file_val}.")
        return -1


def getResult(your_play : RockPaperScissors, elf_play : RockPaperScissors) -> Result:
    SCORING_KEY = [Result.TIE, Result.LOSS, Result.WIN,
                   Result.WIN, Result.TIE, Result.LOSS, 
                   Result.LOSS, Result.WIN, Result.TIE]
    return SCORING_KEY[3*your_play.value + elf_play.value]

def getLineScore(line : str) -> int:
    elf_char = getElfPlay(line[0])
    # space between entries
    your_char = getYourPlay(line[2])

    shape_score = your_char.value + 1 # Indexed from 0, scored from 1
    return getResult(your_char, elf_char).value + shape_score

def getTournamentScore(filename: str) -> int:
    try:
        file = open(filename, 'r')
    except FileNotFoundError:
        print(f"{filename} does not exist")
        return 0
    
    sum_score = 0
    for line in file:
        if not re.search(r"[ABC] [XYZ]", line):
            print(f"Poor line formatting, skipping line {line}")
            continue
        sum_score += getLineScore(line)

    return sum_score

def main(args: list):
    if len(args) != 1:
        print(f"Error: wrong number of arguments. Got {len(args)}, Exected 1.")
        print(f"\tRun with 'python rock_paper_scissors.py <inputfile>'")
        return

    score = getTournamentScore(args[0])

    print(f"Advent of code answer part 1: {score}")


if __name__ == '__main__':
    main(sys.argv[1:])
