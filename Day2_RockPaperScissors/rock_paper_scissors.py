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
        print(f"Invalid XYZ value: {file_val}.")
        return -1

# From the part 1 decoding of the strategy guide
def getXYZRockPaperScissors(file_val: str) -> RockPaperScissors:
    if file_val == "X":
        return  RockPaperScissors.ROCK
    elif file_val == "Y":
        return  RockPaperScissors.PAPER
    elif file_val == "Z":
        return  RockPaperScissors.SCISSORS
    else:
        print(f"Invalid XYZ value: {file_val}.")
        return -1

def getXYZLoseTieWin(file_val: str) -> Result:
    if file_val == "X":
        return Result.LOSS
    elif file_val == "Y":
        return Result.TIE
    elif file_val == "Z":
        return Result.WIN
    else:
        print(f"Invalid XYZ value: {file_val}.")
        return -1

def getYourPlay(elf_play: RockPaperScissors, play_result: Result) -> RockPaperScissors:
    SCORING_KEY = [RockPaperScissors.SCISSORS, RockPaperScissors.ROCK, RockPaperScissors.PAPER,
                   RockPaperScissors.ROCK, RockPaperScissors.PAPER, RockPaperScissors.SCISSORS,
                   RockPaperScissors.PAPER, RockPaperScissors.SCISSORS, RockPaperScissors.ROCK]
    return SCORING_KEY[play_result.value + elf_play.value]

def getXYZLossTieWin(file_val: str) -> RockPaperScissors:
    if file_val == "X":
        return RockPaperScissors.ROCK
    elif file_val == "Y":
        return RockPaperScissors.PAPER
    elif file_val == "Z":
        return RockPaperScissors.SCISSORS
    else:
        print(f"Invalid elf value: {file_val}.")
        return -1

def getResult(your_play: RockPaperScissors, elf_play: RockPaperScissors) -> Result:
    SCORING_KEY = [Result.TIE, Result.LOSS, Result.WIN,
                   Result.WIN, Result.TIE, Result.LOSS,
                   Result.LOSS, Result.WIN, Result.TIE]
    return SCORING_KEY[3*your_play.value + elf_play.value]

def getLineScoreXYZIsYou(line: str) -> int:
    elf_play = getElfPlay(line[0])
    # space between entries
    your_play = getXYZRockPaperScissors(line[2])

    shape_score = your_play.value + 1  # Indexed from 0, scored from 1
    return getResult(your_play, elf_play).value + shape_score

def getLineScoreXYZIsWinLossLose(line: str) -> int:
    elf_play = getElfPlay(line[0])
    # space between entries
    result_play = getXYZLoseTieWin(line[2])
    your_play = getYourPlay(elf_play, result_play)

    shape_score = your_play.value + 1  # Indexed from 0, scored from 1
    return result_play.value + shape_score

def getTournamentScore(filename: str):
    try:
        file = open(filename, 'r')
    except FileNotFoundError:
        print(f"{filename} does not exist")
        return 0

    sum_score_xyz_is_rps = 0
    sum_score_xyz_is_ltw = 0
    for line in file:
        if not re.search(r"[ABC] [XYZ]", line):
            print(f"Poor line formatting, skipping line {line}")
            continue
    
        # If we really cared about efficiency here we'd only parse once and pass to both
        sum_score_xyz_is_rps += getLineScoreXYZIsYou(line)
        sum_score_xyz_is_ltw += getLineScoreXYZIsWinLossLose(line)

    print(f"Advent of code answer part 1: {sum_score_xyz_is_rps}")
    print(f"Advent of code answer part 1: {sum_score_xyz_is_ltw}")


def main(args: list):
    if len(args) != 1:
        print(f"Error: wrong number of arguments. Got {len(args)}, Exected 1.")
        print(f"\tRun with 'python rock_paper_scissors.py <inputfile>'")
        return

    getTournamentScore(args[0])

if __name__ == '__main__':
    main(sys.argv[1:])
