
from pathlib import Path
from math import ceil
import re

input_str: str = ""
p = Path(__file__).with_name("input")
with p.open("r") as f:
    input_str = [x for x in f.read().split("\n")]

stack_count = ceil(len(input_str[1])/4)

offset = 8
stacks: list[list] = [[] for x in range(0, stack_count)]
for x in input_str[:offset]:
    for i in range(1, len(x), 4):
        if x[i] != ' ':
            stacks[i//4].insert(0, x[i])

for x in input_str[offset + 2:]:
    match = re.match(r"move (\d+) from (\d+) to (\d+)", x)
    start = int(match.group(2)) - 1
    end = int(match.group(3)) - 1
    count = int(match.group(1))
    stacks[end].extend(stacks[start][-count:])
    for i in range(0, count):
        stacks[start].pop()

print("".join([x[-1] for x in stacks]))
