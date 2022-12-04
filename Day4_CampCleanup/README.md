# Day 1
[Full description here](https://adventofcode.com/2022/day/4)

### Part 1
Find how many assignment pair ranges completely contain the other
input form "begin1-end1, begin2-end2"

### Thoughts
Regex to quickly pull out integers
* True if `(begin1 <= begin2 && end1 >= end2)` (elf2 range completely contained in elf1 range)
* True if `(begin2 <= begin1 && end2 >= end1)` (elf1 range completely contained in elf2 range)

### Part 2
Find any overlaps

### Thoughts
Basically the same strategy as last time, but it is true if
* `(begin1 >= begin2 && begin1 <= end2)` (elf1 range starts within elf2 range)
* `(end1 >= begin2 && end1 <= end2)` (elf1 range ends within elf2 range)
Error: This does not catch elf2 range completely within elf1 range. Can add additional check, or reduce by checking the 'else' conditions:
Given Elf1Range = [A, B], Elf2Range=[C, D]
Overlap if order not A, B, C, D or C, D, A, B
* `If not B < C or D < A`