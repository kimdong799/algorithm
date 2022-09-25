# 너비 우선 탐색

import sys

n, m = map(int, sys.stdin.readline().split())
input = sys.stdin.readline
maze = []

for _ in range(n):
    maze.append(list(map(int, input().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = [[0, 0]]

while queue:
    x, y = queue[0][0], queue[0][1]
    del queue[0]

    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and ny >= 0 and nx < n and ny < m:
            if maze[nx][ny] == 1:
                queue.append([nx, ny])
                maze[nx][ny] = maze[x][y] + 1
print(maze[-1][-1])