# 알고리즘 분류 : Dynamic Programming
# Dynamic Programming(동적계획법)이란?
# 하나의 문제는 단 한 번만 풀도록 하는 알고리즘이다.
# DP는 다음의 문제에서 사용 가능하다.
# 1. 큰 문제를 작은 문제로 나눌 수 있다. 
# 2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.
# DP가 분할 정복과 다른 점은 이미 계산한 결과는 배열에 저장하여 사용한다는 점이다.


import sys

N = int(sys.stdin.readline())

# 계산횟수 배열 init
dp = [0]*(N+1)

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    # 2나 3은 1로 만들기 위해 1번이 필요함, 즉 2와 3의 배수인 경우
    # 2나 3이 필요로 하는 연산 횟수에 1을 더하면 된다.
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
print(dp[N])    