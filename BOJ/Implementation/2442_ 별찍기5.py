N = int(input())

for i in range(1, N+1):
    line = ' ' * (N-i) + '*' * ((2*i)-1)
    print(line)