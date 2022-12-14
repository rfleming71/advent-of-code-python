
from pathlib import Path
from numpy import array, copy, rot90

input: str = ""
p = Path(__file__).with_name("input")
with p.open("r") as f:
    input = [
        [int(i) for i in x.strip()] for x in f.read().split("\n")
    ]

input = array(input)

visible = array([[1] * len(input[0]) for x in input])

for _ in range(4):
    input = rot90(input)
    visible = rot90(visible)
    for yid, y in enumerate(input):
        for x_start, tree in enumerate(y):
            count = 0
            if x_start + 1 < len(y):
                for next in input[yid][x_start + 1:]:
                    count += 1
                    if next >= tree:
                        break

            visible[yid][x_start] *= count

print(max([max(x) for x in visible]))
