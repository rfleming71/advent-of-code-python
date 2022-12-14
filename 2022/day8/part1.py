
from pathlib import Path
from numpy import array, copy, rot90

input: str = ""
p = Path(__file__).with_name("input")
with p.open("r") as f:
    input = [
        [int(i) for i in x.strip()] for x in f.read().split("\n")
    ]

input = array(input)

visible = array([[0] * len(input[0]) for x in input])

for _ in range(4):
    input = rot90(input)
    visible = rot90(visible)
    for y in range(len(input)):
        last = -1
        for x in range(len(input[y])):
            tree = input[y][x]
            if tree > last:
                visible[y][x] = 1
                last = tree

print(sum([sum(x) for x in visible]))
