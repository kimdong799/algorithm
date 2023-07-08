import sys
from collections import deque

N = int(sys.stdin.readline())

cards = deque(range(1, N+1))

while cards:
    if len(cards)==1:
        break
    cards.popleft()
    cards.append(cards.popleft())
print(cards[0])