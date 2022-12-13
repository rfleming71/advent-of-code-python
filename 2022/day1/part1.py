
from pathlib import Path

input_str: str = ""
p = Path(__file__).with_name("input")
with p.open("r") as f:
    input_str = [x.strip() for x in f.read().split("\n")]

current_elf = 0
max_elf = 0
for i in input_str:
    if i == "":
        if current_elf > max_elf:
            max_elf = current_elf
        current_elf = 0
    else:
        current_elf += int(i)

print(max_elf)
