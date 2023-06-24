import sys

n = int(sys.stdin.readline())

nums = []
[nums.append(int(sys.stdin.readline())) for _ in range(n)]

nums.sort()
[print(num) for num in nums]

# Bubble Sort Solution
# n = len(nums)
# def bubblesort(nums):
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if nums[j] > nums[j+1]:
#                 nums[j], nums[j+1] = nums[j+1], nums[j]
#     return nums

# nums = bubblesort(nums)
# [print(num) for num in nums]