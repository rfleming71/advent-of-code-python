
from pathlib import Path
from functools import cmp_to_key

input: str = ""
p = Path(__file__).with_name("input")
with p.open("r") as f:
    input = [x.strip() for x in f.read().split("\n")]

pairs = [eval(x) for x in input if x != ""]
pairs.append([[2]])
pairs.append([[6]])


def compare_list(left: list, right: list) -> int:
    for i, _ in enumerate(left):
        if i >= len(right):
            return -1

        left_value = left[i]
        right_value = right[i]
        if not isinstance(left_value, type(right[i])):
            if not isinstance(left_value, list):
                left_value = [left_value]
            else:
                right_value = [right_value]

        if isinstance(left_value, int):
            if left_value != right_value:
                return 1 if left_value < right_value else -1
        elif isinstance(left_value, list):
            res = compare_list(left_value, right_value)
            if res != 0:
                return res

    if len(left) < len(right):
        return 1

    return 0


pairs = sorted(pairs, key=cmp_to_key(compare_list))
pairs.reverse()
result = 1
for (idx, id) in enumerate(pairs):
    if id == [[2]] or id == [[6]]:
        result *= idx + 1

print(result)
