import sys

nums = list(map(int, sys.stdin.readline().split()))
nums = [num**2 for num in nums]
print(sum(nums)%10)