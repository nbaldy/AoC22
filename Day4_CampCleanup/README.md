# Day 1
[Full description here](https://adventofcode.com/2022/day/4)

### Part 1
Find how many assignment pair ranges completely contain the other
input form "begin1-end1, begin2-end2"

### Thoughts
Regex to quickly pull out integers
* True if `(begin1 <= begin2 && end1 >= end2)` (elf2 range completely contained in elf1 range)
* True if `(begin2 <= begin1 && end2 >= end1)` (elf1 range completely contained in elf2 range)
