# Day 5
[Full description here](https://adventofcode.com/2022/day/5)

### Part 1
Rearrange a bunch of crates according to instructions

### Thoughts
Regex to quickly pull out important info

Definitely need some stacks. Just use python lists - create based on number of characters in the line / 4 (because letter, brackets, space). Add to a list. When we get to the all number line, reverse that list. 

Could I do this with regex? Probably. Will I? Probably not.

```
line = file.readline()
num_elems = len(line) // 4
crate_stack = [[]]*num_elems
while '[' == line[0]:
    for row in range(num_elems):
        # Because we are not initializing in the right order yet
        crate_stack[row].append(line[4*row])

    # Setup for next iter
    line = file.readline()
    if len(line) != num_elems: 
        print(f"Inconsistent stack lengths! Expect {num_elems} got {len(line)//4}: {line}")
```

The following line is just a format check
```
if num_elems != int(line.strip()[-1]):
    print(f"Inconsistent stack lengths! Expect {num_elems} got {line.strip()[-1]}: {line}")
```

Then follow the instructions after regex parse
```
match = re.find(move_line_regex, line)
num_to_move, col_from, col_to = match.groups()
if col_from > num_elems or col_to > num_elems:
    print(f"bad move {line}, only {num_elems} elements")
for crate in range(num_to_move):
    crate_stacks[col_to].append(crate_stacks[col_from].pop())
```

Probably shouldn't have writen so much code out, since I got distracted and am now 7 days late.

Arg, so I do need regex for that first one, or else it's difficult to differentiate between no first element and the "number" line

Arg my regex limits have been tested. Actually just go back to reading every x; spaces are throwing me off.