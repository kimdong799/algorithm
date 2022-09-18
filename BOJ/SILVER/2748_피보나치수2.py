import sys

N = int(sys.stdin.readline())

dp = [0]*(N+1)

# 피보나치 함수
def fibonacci(num):
    if (num==0):
        return 0
    elif (num==1):
        return 1
    elif (num==2):
        return 1
    else:
        return dp[num-1] + dp[num-2]

for i in range(N+1):
    dp[i] = fibonacci(i)

print(dp[N])