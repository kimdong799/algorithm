# 난이도 하 / 풀이시간 30분 / 시간제한 1초 / 메모리제한 128MB / 기출 2019 국가 교육기관 코테

# 주어진 배열을 이용해 가장 큰 수를 만들어라.
# N크기의 배열을 이요해 M번 원소를 더하고 같은 수는 최대 K번 더할 수 있다.

# 공백 구분 입력받기
n, m, k = map(int, input().split())
input_arr = sorted(list(map(int, input().split())), reverse=True)

first, second = input_arr[0], input_arr[1]
result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1
print(result)

# 개선된 풀이방식
n, m, k = map(int, input().split())
input_arr = sorted(list(map(int, input().split())), reverse=True)
first, second = input_arr[0], input_arr[1]
result = 0

# 수열이 반복되는 횟수 * k번 = 가장 큰 수가 더해진 횟수
count = (m // (k + 1)) * k
# 수열이 딱 떨어지지 않는 경우 예외처리
count += m % (k + 1)

result += (count) * first
result += (m - count) * second
print(result)
