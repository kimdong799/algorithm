'''
피제수(분자) A와 제수(분모) B가 있다. 두 수를 나누었을 때, 소숫점 아래 N번째 자리수를 구하려고 한다. 예를 들어, A=3, B=4, N=1이라면, A÷B=0.75 이므로 출력 값은 7이 된다.
'''

import sys

a, b, n = map(int, sys.stdin.readline().split())

for i in range(n):
    a = (a%b)*10
    result = a//b
print(result)
