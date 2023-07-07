import sys
from collections import deque

N, K = map(int,sys.stdin.readline().split())
deq = deque(list(range(1, N+1)))

result = []

while deq:
    for i in range(K-1):
        deq.append(deq.popleft())
    result.append(deq.popleft())

print("<", end='')
print(', '.join(map(str,result)), end='')
print(">")