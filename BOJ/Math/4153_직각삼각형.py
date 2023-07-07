import sys

triangles = []

while True:
    lines = list(map(int, sys.stdin.readline().split()))
    if lines == [0, 0, 0]:
        break
    else:
        triangles.append(lines)

for triangle in triangles:
    sum_ = 0
    max_value = max(triangle)
    triangle.remove(max_value)
    for line in triangle:
        sum_ += line**2
    if sum_ == max_value**2:
        print("right")
    else:
        print("wrong")