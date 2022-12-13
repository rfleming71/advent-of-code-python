
from pathlib import Path

input_str: str = ""
p = Path(__file__).with_name("input")
with p.open("r") as f:
    input_str = [x.strip() for x in f.read().split("\n")]

scores = {"X": 1, "Y": 2, "Z": 3}

lookup = {"X": "A", "Y": "B", "Z": "C"}


def score_round(op, elf) -> int:
    elf = lookup[elf]
    if op == elf:
        return 3

    if (op == "A" and elf == "B") or (op == "B" and elf == "C") or (op == "C" and elf == "A"):
        return 6

    return 0


score = 0
for i in input_str:
    opponent = i[0]
    elf = i[2]
    score += scores[elf] + score_round(opponent, elf)


print(score)
