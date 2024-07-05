"""
1. 그리디 알고리즘은 현재 상황에서 지금 당장 좋은 것만 고르는 방법
2. 알고리즘 문제에서 '가장 큰 순서대로', '가장 작은 순서대로'와 같은 기준을 알게 모르게 제시해준다.
"""

# 거스름돈으로 사용할 500, 100, 50, 10원 동전이 문한히 존재한다고 가정한다.
# 손님에게 거슬러 줘야 하는 돈이 N원일 때 거슬러줘야 할 동전의 최소 개수를 구하라.
# 거슬러 줘야 할 돈 N은 항상 10의 배수이다.

# 가장 큰 화폐 단위부터 돈을 거슬러줘보자.
# 거슬러 준 동전의 갯수는?

# 최초 풀이
n = 1260
coins = [500, 100, 50, 10]
idx = 0
count = 0
while n:
    if n >= coins[idx]:
        n -= coins[idx]
        print(f"{coins[idx]}를 거슬러주었습니다.")
        count += 1
    else:
        idx += 1
print(f"result : {count}")

# 예제 풀이
n = 1260
coins = [500, 100, 50, 10]
count = 0
for coin in coins:
    count += n // coin
    n %= coin
print(f"result : {count}")
