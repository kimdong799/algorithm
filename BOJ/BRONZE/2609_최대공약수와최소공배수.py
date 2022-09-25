'''
첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.
첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.
'''
# 유클리드 호제법

import sys

a, b = map(int, sys.stdin.readline().split())

def get_gcd(a, b):
    if b==0:
        return a
    else:
        return get_gcd(b, a%b)

gcd = get_gcd(a, b)
lcm = int((a * b / gcd))

sys.stdout.write(str(gcd)+'\n')
sys.stdout.write(str(lcm))