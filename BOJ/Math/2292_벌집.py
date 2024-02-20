import sys

N = int(sys.stdin.readline())
cnt = 1
while N > 0:
    if N <= 1:
        print(cnt)
        break
    else:
        N = N - 6 * cnt
        cnt += 1
else:
    print(cnt)
