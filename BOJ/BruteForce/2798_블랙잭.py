import sys

N, M = map(int,sys.stdin.readline().split())
cards = list(map(int,sys.stdin.readline().split()))

max_num = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if(cards[i] + cards[j] + cards[k]> M):
                continue
            else:
                max_num = max(max_num, cards[i] + cards[j] + cards[k])
print(max_num)