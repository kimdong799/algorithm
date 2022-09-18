import sys

N = int(sys.stdin.readline())

# in 연산은 set이 list보다 최적화됨
A = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
input_nums = list(map(int, sys.stdin.readline().split()))

[print(1) if i in A else print(0) for i in input_nums]