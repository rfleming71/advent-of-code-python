
from pathlib import Path

input_str: str = ""
p = Path(__file__).with_name("input")
with p.open("r") as f:
    input_str = [x.strip() for x in f.read().split("\n")]

scores = {"A": 1, "B": 2, "C": 3}

lookup = ["A", "B", "C"]


score = 0
for i in input_str:
    opponent = i[0]
    elf = i[2]
    if elf == "X":
        elf = lookup[(lookup.index(opponent) - 1)]
    elif elf == "Y":
        elf = opponent[0]
        score += 3
    else:
        elf = lookup[(lookup.index(opponent) + 1) % len(lookup)]
        score += 6

    score += scores[elf]


print(score)
