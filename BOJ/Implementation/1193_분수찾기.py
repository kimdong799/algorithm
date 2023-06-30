import sys

# init
n = int(sys.stdin.readline())
line = 1
line_sum = 0

while n > line:
    n -= line
    line += 1

if line % 2 == 0:
    num1 = n
    num2 = line - n + 1
else:
    num1 = line - n + 1
    num2 = n
print(f"{num1}/{num2}")