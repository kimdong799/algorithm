n = int(input())
plans = input().split()
x, y = 1, 1

move_types = ["L", "R", "U", "D"]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for move in plans:
    for i in range(len(move_types)):
        if move == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 배열 범위 검증
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
print(f"{x} {y}")
