import sys

n = int(sys.stdin.readline())

class Size:
    def __init__(self, idx, weight, height):
        self.idx = int(idx)
        self.weight = int(weight)
        self.height = int(height)

size_list = []
for idx in range(n):
    weight, height = sys.stdin.readline().strip().split()
    size = Size(idx, weight, height)
    size_list.append(size)

ranks = []
for i in range(n):
    rank = 1
    for j in range(n):
        if i == j:
            continue 
        elif size_list[i].weight < size_list[j].weight and size_list[i].height < size_list[j].height:
            rank += 1
    ranks.append(rank)

print(*ranks)