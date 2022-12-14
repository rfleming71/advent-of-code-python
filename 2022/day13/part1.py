
from pathlib import Path

input: str = ""
p = Path(__file__).with_name("input")
with p.open("r") as f:
    input = [x.strip() for x in f.read().split("\n")]

pairs = [input[x:x + 2] for x in range(0, len(input) + 1, 3)]


def compare_list(left: list, right: list) -> int:
    for i, _ in enumerate(left):
        if i >= len(right):
            return -1

        if not isinstance(left[i], type(right[i])):
            if not isinstance(left[i], list):
                left[i] = [left[i]]
            else:
                right[i] = [right[i]]

        if isinstance(left[i], int):
            if left[i] != right[i]:
                return 1 if left[i] < right[i] else -1
        elif isinstance(left[i], list):
            res = compare_list(left[i], right[i])
            if res != 0:
                return res

    if len(left) < len(right):
        return 1

    return 0


count = 0
for idx, pair in enumerate(pairs):
    left = eval(pair[0])
    right = eval(pair[1])
    res = compare_list(left, right)
    if res != -1:
        count += idx + 1

print(count)
