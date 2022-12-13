
from pathlib import Path
import string

input_str: str = ""
p = Path(__file__).with_name("input")
with p.open("r") as f:
    input_str = [x.strip() for x in f.read().split("\n")]

score = 0
for (left, right) in [(x[:len(x)//2], x[len(x)//2:]) for x in input_str]:
    overlap = set([x for x in left if x in right])
    for x in overlap:
        if x in string.ascii_lowercase:
            score += ord(x) - 96
        else:
            score += ord(x) - 38


print(score)
