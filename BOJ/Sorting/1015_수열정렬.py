# P[0], P[1], ...., P[N-1]은 0부터 N-1까지(포함)의 수를 한 번씩 포함하고 있는 수열이다. 수열 P를 길이가 N인 배열 A에 적용하면 길이가 N인 배열 B가 된다. 적용하는 방법은 B[P[i]] = A[i]이다.
# 배열 A가 주어졌을 때, 수열 P를 적용한 결과가 비내림차순이 되는 수열을 찾는 프로그램을 작성하시오. 비내림차순이란, 각각의 원소가 바로 앞에 있는 원소보다 크거나 같을 경우를 말한다. 만약 그러한 수열이 여러개라면 사전순으로 앞서는 것을 출력한다.

import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

b = [0] * n
sorted_a = sorted(a)

p = []
for i in a:
    p.append(sorted_a.index(i))
    # 이미 할당한 숫자는 sorted_A에서 -1로 대채해 재탐색되지 않도록 함.
    sorted_a[sorted_a.index(i)] = -1
 
results = [i for i in p]

for result in results:
    sys.stdout.write(str(result)+' ')
