import sys

t = int(sys.stdin.readline())
for case in range(t):
    h, w, n = list(map(int, sys.stdin.readline().split()))
    cnt = 0
    for i in range(w):
        for j in range(h):
            cnt += 1
            if cnt == n:
                formatted_number = "{:02d}".format(i+1)
                print(f"{j+1}{formatted_number}")
