import sys

T = int(sys.stdin.readline())

# 피보나치 함수
def fibonacci(num):
    if (num == 0):
        zero_arr[0] = 1
        one_arr[0] = 0
    else:
        zero_arr[num] = one_arr[num-1]
        one_arr[num] = zero_arr[num-1] + one_arr[num-1]

for _ in range(T):
    N = int(sys.stdin.readline())

    # dp arr init

    zero_arr = [0] * (N + 1)
    one_arr = [0] * (N + 1)


    for i in range(N+1):
        fibonacci(i)
    # print("{} / zero : {} / one : {}".format(N, zero_arr[N], one_arr[N]))
    print("{} {}".format(zero_arr[N] ,one_arr[N]))