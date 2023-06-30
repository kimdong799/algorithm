'''
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
'''

import sys
from collections import deque

# n = 정점의 갯수
# m = 간선의 개수
# v = 시작 노드 값

n, m, start = map(int, sys.stdin.readline().split())

# input graph
graph = [[] for _ in range(n+1)]
graph[0] = [0,0]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# graph sort
[i.sort() for i in graph]

print(graph)

visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

def dfs(idx):
    visited_dfs[idx] = True
    print(idx, end=' ')
    for i in graph[idx]:
        if not visited_dfs[i]:
            dfs(i)

queue = deque()

def bfs(start):
    queue.append(start)
    visited_bfs[start] = True
    while queue:
        idx = queue.popleft()
        print(idx, end=' ')
        for i in graph[idx]:
            if not visited_bfs[i]:
                visited_bfs[i] = True
                queue.append(i)

dfs(start)
print()
bfs(start)