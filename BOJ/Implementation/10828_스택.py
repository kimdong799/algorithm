import sys

n = int(sys.stdin.readline().strip())
methods = []
[methods.append(sys.stdin.readline().strip()) for _ in range(n)]
stack = []

for method in methods:
    func = method.split()[0]
    if func == "push":
        stack.append(method.split()[1])
    elif func == "top":
        if len(stack)==0:
            print("-1")
        else:
            print(stack[-1])
    elif func == "size":
        print(len(stack))
    elif func == "empty":
        if len(stack)==0:
            print("1")
        else:
            print("0")
    elif func == "pop":
        if len(stack)==0:
            print("-1")
        else:
            print(stack.pop())