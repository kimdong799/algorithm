import sys

nums = list(map(int, sys.stdin.readline().split()))

nums.sort()

diff = min(nums[1] - nums[0], nums[2] - nums[1])

for i in range(len(nums)):
    temp = nums[i]
    if temp + diff not in nums:
        print(temp+diff)
        break