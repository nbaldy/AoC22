# Day 1
[Full description here](https://adventofcode.com/2022/day/1)

### Part 1
Find the duplicate items (case sensitive) in each half of the rucksack and sum their 'priorities' 

* [a-z] = [1-26]
* [A-Z] = [27-52]

### Thoughts
At this stage, item priorities are not used to actually reorganize

Seems simple enough, split the string into halves and bucket sort the halves (since we aren't reorganizing, this is faster than building a map, especially since we have continuous keys explicitly baked into the problem)
