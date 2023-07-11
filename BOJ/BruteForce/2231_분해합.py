import sys

N = int(sys.stdin.readline())
num_chars = list(str(N))

results = []
for i in range(1, N+1):
    num = sum(map(int, list(str(i))))
    num_sum = i + num
    if num_sum == N:
        print(i)
        break
if i == N:
    print(0)