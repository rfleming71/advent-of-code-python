
from pathlib import Path
import string

input_str: str = ""
p = Path(__file__).with_name("input")
with p.open("r") as f:
    input_str = [x.strip() for x in f.read().split("\n")]


def build_range(input: str) -> list:
    (start, end) = [int(x) for x in input.split("-")]
    return list(range(start, end + 1))


score = 0
for (left, right) in [x.split(",") for x in input_str]:
    left = build_range(left)
    right = build_range(right)
    if any(item in left for item in right):
        score += 1


print(score)
