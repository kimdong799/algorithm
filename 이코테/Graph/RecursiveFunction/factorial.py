# 재귀함수를 이용하여 팩토리얼 구현

# ex) factorial(5) = 5 * 4 * 3 * 2 * 1


# 내가 구현한 재귀함수
def factorial(num):
    print(f"prameter : {num}")
    if num != 1:
        num *= factorial(num - 1)
    return num


print(factorial(5))


# 책에 나온 재귀함수 에제
def factorial_ex(num):
    if num <= 1:
        return 1
    return num * factorial_ex(num - 1)
