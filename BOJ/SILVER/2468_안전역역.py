from collections import deque
import sys

sys.setrecursionlimit(100000)

n = int(sys.stdin.readline()) # graph의 행과 열을 나타내는 수
graph = []
max_num = 0
result = 1

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

# print(graph)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# BFS
def bfs(x, y, h):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()
         
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > h and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
    return

for h in range(100):
    cnt = 0
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(len(graph[i])):
            if visited[i][j] == 0 and graph[i][j] > h:
                bfs(i, j, h)
                cnt += 1
    result = max(result, cnt)
print(result)

# DFS
def dfs(x, y, h):
    visited[x][y] = 1

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] > h and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                dfs(nx, ny, h)
    return

for h in range(100):
    cnt = 0
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(len(graph[i])):
            if visited[i][j] == 0 and graph[i][j] > h:
                dfs(i, j, h)
                cnt += 1
    result = max(result, cnt)
print(result)
