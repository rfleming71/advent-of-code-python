
from pathlib import Path

input_str: str = ""
p = Path(__file__).with_name("input")
with p.open("r") as f:
    input_str = [x.strip() for x in f.read().split("\n")]

elves: list[int] = []

current_elf = 0
for i in input_str:
    if i == "":
        if current_elf > 0:
            elves.append(current_elf)
        current_elf = 0
    else:
        current_elf += int(i)

elves.sort()
print(sum(elves[-3:]))
