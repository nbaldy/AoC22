# Day 1
[Full description here](https://adventofcode.com/2022/day/2)

### Part 1
Calculate the score for a rock paper scissors game if the strategy is followed. 
Scoring occurs as the following:
Shape points (individual):
    - 1 point for playing Rock (X)
    - 2 points for playing paper (Y)
    - 3 points for playing scissors (Z)

Win points (dependent on opponent):
    - 0 points for loss
    - 3 points for tie
    - 6 points for win

### Thought process
Diagram:
| You  | Key | Elf | Key | Your Score + Comments |
| ---  | --- | --- | --- | --------------------- | 
|**X** | _R_ |**A**| _R_ |  4 (1 ind + 3 tie)
|**X** | _R_ |**B**| _P_ |  1 (1 ind + 0 loss )
|**X** | _R_ |**C**| _S_ |  7 (1 ind + 6 win)
|**Y** | _P_ |**A**| _R_ |  8 (2 ind + 6 win)
|**Y** | _P_ |**B**| _P_ |  5 (2 ind + 3 tie)
|**Y** | _P_ |**C**| _S_ |  2 (2 ind + 0 loss)
|**Z** | _S_ |**A**| _R_ |  4 (3 ind + 0 loss)
|**Z** | _S_ |**B**| _P_ |  9 (3 ind + 6 win)
|**Z** | _S_ |**C**| _S_ |  6 (3 ind + 3 tie)

Make score lookup table for win/lose
3*You + Elf = index
[tie, loss, win, win, tie, loss, loss, win, tie]

### Part 2
- X means you need to lose
- Y means you need to tie
- Z means you need to win
