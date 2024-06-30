n, k = map(int, input().split())


def func1(n):
    result = n - 1
    print(f"func1 - {result}")
    return result


def func2(n, k):
    result = n / k
    print(f"func2 - {n/k}")
    return result


count = 0
while True:
    if n == 1:
        break
    else:
        if n % k == 0:
            n = func2(n, k)
            count += 1
        else:
            n = func1(n)
            count += 1
print(count)
