# DFS, BFS를 구현하기 위해 재귀함수에 대한 이해가 필요
# 재귀함수(Recusive Function)란 자기 자신을 다시 호출하는 함수를 의미한다.

cnt = 1


def recursive_function(cnt):
    print(f"[{cnt}] - 재귀 함수를 호출합니다.")
    cnt += 1
    if cnt <= 10:
        recursive_function(cnt)


recursive_function(cnt)
