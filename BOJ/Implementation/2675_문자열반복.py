import sys

cnt = int(sys.stdin.readline().rstrip())
for _ in range(0, cnt):
    R, S = map(str, sys.stdin.readline().split())
    P = ""

    for i in S:
        for _ in range(0, int(R)):
            P += i
    print(P)