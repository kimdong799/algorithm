import sys

n = int(sys.stdin.readline())

class pipeline:
    def __init__(self, first, second):
        self.first = int(first)
        self.second = int(second)

data_list = []
for i in range(n):
    first, second = sys.stdin.readline().strip().split()
    data = pipeline(first, second)
    data_list.append(data)
data_list.sort(key=lambda x: (x.first, x.second))

[print(f"{data.first} {data.second}") for data in data_list]