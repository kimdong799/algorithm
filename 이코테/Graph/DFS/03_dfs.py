"""
DFS는 깊이 우선 탐색으로 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘.
스택 자료구조(혹은 재귀함수)를 이용한다.

1. 탐색 시작 노드를 스택에 삽입하고 방문처리
2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있다면
   그 노드를 스택에 넣고 방문처리.
   방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄.
3. 2번의 과정을 수행할 수 없을 때까지 반복.
"""

def dfs(graph, v, visited):
  # 방문처리
  visited[v] = True
  print(v, end=' ')
  
  # 그래프 순회
  for i in graph[v]:
    # 방문하지 않은 노드라면 재귀함수 호출
    if not visited[i]:
      dfs(graph, i, visited)
      
# 노드 번호와 Index를 맞춰주기 위해 첫칸 비워둠
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

visited = [False] * len(graph)

dfs(graph, 1, visited)