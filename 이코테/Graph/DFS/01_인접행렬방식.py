# DFS는 Depth-First Search, 깊이 우선 탐색이라고 부름.
# 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘

# 인접 행렬(Adjacenct Matrix) : 2차원 배열로 그래프의 연결 관계를 표현
# 인접 리스트(Adjacency List) : 리스트로 그래프의 연결 관계를 표현하는 방식

# 인접행렬 방식은 2차원 배열에 각 노드가 연결된 형태를 기록하는 방식.
# 연결되지 않은 노드는 무한의 비용으로 작성

INF = 999999999  # 무한의 비용 선언

# 2차원 리스트를 이용해 인접 행렬 표현
graph = [[0, 7, 5], [7, 0, INF], [5, INF, 0]]

print(graph)
