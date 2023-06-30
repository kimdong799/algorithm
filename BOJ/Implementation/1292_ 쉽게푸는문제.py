import sys
nums = list(map(int, sys.stdin.readline().split()))

arr = [0]

for i in range(1, 1001):
    for j in range(i):
        arr.append(i)
 
result = sum(arr[nums[0]:nums[1]+1])
print(result)
