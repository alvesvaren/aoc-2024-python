from aoc import get_input
from re import compile

data = get_input(3)

part1 = 0
part2 = 0

pattern = compile(r"mul\((\d{1,3}),(\d{1,3})\)")

disables = data.split("don't()")

parts = [disables[0]]

for disable in disables:
    start = disable.find("do()")
    parts.append(disable[start:])

for match in pattern.finditer(data):
    a, b = map(int, match.groups())
    part1 += a * b

for match in pattern.finditer("".join(parts)):
    a, b = map(int, match.groups())
    part2 += a * b

print("Part 1:", part1)
print("Part 2:", part2)
