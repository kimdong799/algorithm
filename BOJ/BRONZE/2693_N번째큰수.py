# 배열 A가 주어졌을 때, N번째 큰 값을 출력하는 프로그램을 작성하시오.
# 배열 A의 크기는 항상 10이고, 자연수만 가지고 있다. N은 항상 3이다.

# 각 테스트 케이스에 대해 한 줄에 하나씩 배열 A에서 3번째 큰 값을 출력한다.

import sys

T = int(sys.stdin.readline())
result = []
for _ in range(T):
    nums = list(map(int, sys.stdin.readline().split()))
    nums.sort()
    result.append(nums[-3])

[print(r) for r in result]