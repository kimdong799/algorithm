import sys
from collections import deque

deq = deque()
n = int(sys.stdin.readline().strip())
methods = []
[methods.append(sys.stdin.readline().strip()) for _ in range(n)]

for method in methods:
    func = method.split()[0]
    if func == "push":
        deq.append(method.split()[1])
    elif func == "front":
        if len(deq)==0:
            print("-1")
        else:
            print(deq[0])
    elif func == "back":
        if len(deq)==0:
            print("-1")
        else:
            print(deq[-1])
    elif func == "size":
        print(len(deq))
    elif func == "empty":
        if len(deq)==0:
            print("1")
        else:
            print("0")
    elif func == "pop":
        if len(deq)==0:
            print("-1")
        else:
            print(deq.popleft())