from aoc import get_input

data = get_input(2)

part1 = 0
part2 = 0

def safe(nums: list[int]):
  if nums[0] < nums[1]:
    nums = nums[::-1]

  for a,b in zip(nums, nums[1:]):
    d = a - b
    if d > 3 or d < 1:
      return False

  return True

for row in data.splitlines():
  nums = row.split(" ")
  nums = list(map(int, nums))

  if safe(nums):
    part1 += 1
  
  for i in range(len(nums)):
    if safe(nums[:i] + nums[i+1:]):
      part2 += 1
      break


print("Part 1:", part1)
print("Part 2:", part2)
