# nx, ny 방법으로 풀이
# 해설의 경우 steps를 이용해 [(), ()...] 형태의 이동 방향을 정하고 시뮬레이션

start = input()

count = 0

col_dic = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}

y = col_dic[start[0]]
x = int(start[1])


move_types = [
    "L1",
    "L2",
    "R1",
    "R2",
    "U1",
    "U2",
    "D1",
    "D2",
]

nx = [-1, 1, -1, 1, -2, -2, 2, 2]

ny = [-2, -2, 2, 2, 1, -1, 1, -1]

for move_idx in range(len(move_types)):

    if (
        x + nx[move_idx] < 1
        or y + ny[move_idx] < 1
        or x + nx[move_idx] > 9
        or y + ny[move_idx] > 9
    ):
        continue
    else:
        print(move_types[move_idx])
        count += 1
print(count)
