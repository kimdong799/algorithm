import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph =[]
for i in range(n):
    graph.append(list(map(int, input())))

visited_bfs = [[False] * m for _ in range(n)]

# 상하좌우 탐색
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    if graph [x][y] == 1:
        return False

    while q:
        x, y = q.popleft()
        graph[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                q.append((nx, ny))
    return True

cnt = 0

for i in range(n):
    for j in range(m):
        # 현재 위치에서 BFS 수행
        if bfs(i, j) == True:
            cnt += 1

print(cnt)