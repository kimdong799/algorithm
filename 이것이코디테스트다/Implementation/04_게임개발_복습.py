n, m = map(int, input().split())
x, y, direction = map(int, input().split())

# 히스토리 맵 생성 (가본 곳 확인 용)
history = [[0] * m for _ in range(n)]

# 맵 입력
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

# 북 동 남 서 (시계방향))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

turn_count = 1


def turn_left():
    # 글로벌 변수로 선언
    global direction
    global turn_count
    direction -= 1
    turn_count += 1
    if direction == -1:
        direction = 3


# 시작점 방문처리
history[x][y] = 1
count = 1

# 시뮬레이션
while True:
    # 현재 방향에서 왼족 방향으로 전환
    turn_left()

    nx = x + dx[direction]
    ny = y + dy[direction]

    # 미방문 칸 발견
    if history[nx][ny] == 0 and arr[nx][ny] == 0:
        x = nx
        y = ny
        # 방문처리
        history[nx][ny] = 1
        count += 1
        # 회전 횟수 초기화
        turn_count = 1
        continue
    else:
        if turn_count == 4:
            # 모두 방문했다면 뒤로 이동
            nx = x - dx[direction]
            ny = y - dy[direction]
            # 뒤가 바다인 경우 종료
            if arr[nx][ny] == 1:
                break
            else:
                x = nx
                y = ny
print(count)
