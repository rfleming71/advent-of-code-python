
from pathlib import Path
import string

input_str: str = ""
p = Path(__file__).with_name("input")
with p.open("r") as f:
    input_str = [x.strip() for x in f.read().split("\n")]


groups = [[set(i) for i in input_str[x:x+3]] for x in range(0, len(input_str), 3)]

score = 0
for x in groups:
    item = x[0].intersection(x[1], x[2])
    for i in item:
        if i in string.ascii_lowercase:
            score += ord(i) - 96
        else:
            score += ord(i) - 38

print(score)
