# Day 1
[Full description here](https://adventofcode.com/2022/day/1)

### Part 1
Count the number of 'calories' carried by each elf, separated by newlines - compute the maximum calories carried by an elf. 

### Thought process
I really don't think there's a way to do this other than O(n) since there's no sorting here and sorting it would be more expensive than just traversing. So I think the best solution is probably the simplest - iterate through the lines of a file; if there's a newline it starts a new entry. If this new entry is larger than the largest, replace the largest. 

No need to cache results - this could easily be added later if the puzzle boundaries changed. 

Because I decided to use python to focus on the algorithm, the input process is super simple too, I think.

### Part2 
Get the top 3 elves and calories

### Thought process
Just modify part 1 - it still works for part 1, but give it instead a buffer of 3 elves. Make this a priority queue such that the elf with the fewest always floats to the top so that we pop them first. 

For a priority queue, use python heapq. I need to figure out how this sorts if I want to keep the elf number in there. Looks like I just make Elf a class and define `_lt_`.
