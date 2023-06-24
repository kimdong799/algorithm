import sys

n = int(sys.stdin.readline().strip())

def get_hansu(n):
    cnt = 0
    for i in range(1, n+1):
        num_list = list(map(int,str(i)))
        if i < 100:
            cnt += 1
        elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
            cnt += 1
    return cnt

cnt = get_hansu(n)
print(cnt)