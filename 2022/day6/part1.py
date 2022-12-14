
from pathlib import Path

input_str: str = ""
p = Path(__file__).with_name("input")
with p.open("r") as f:
    input_str = f.read().strip()

chunks = [(x, set(input_str[x:4])) for x in range(0, len(input_str) - 4)]

for x in range(0, len(input_str) - 4):
    letters = set(input_str[x:x + 4])
    if len(letters) == 4:
        print(x + 4)
        break
