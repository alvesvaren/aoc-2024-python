from aoc import get_input
import re

data = get_input(1)

pattern = re.compile(r"(\d+)   (\d+)")

col1 = []
col2 = []

for row in data.splitlines():
    match = pattern.match(row)

    if match:
        a, b = match.groups()
        col1.append(int(a))
        col2.append(int(b))

col1.sort()
col2.sort()

total1 = 0
for a, b in zip(col1, col2):
    total1 += abs(a - b)


col2_counts = {}

for i in col2:
    col2_counts[i] = col2_counts.get(i, 0) + 1

total2 = 0
for i in col1:
    total2 += i * col2_counts.get(i, 0)

print("Part 1:", total1)
print("Part 2:", total2)
