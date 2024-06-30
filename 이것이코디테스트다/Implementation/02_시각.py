n = int(input())

count = 0
hour = 0
minute = 0
second = 0
trgt_char = "3"

for i in range(3600 * n + 3600):
    second += 1
    if second >= 60:
        minute += 1
        second = 0
    if minute >= 60:
        hour += 1
        minute = 0
    # print(f"{hour}:{minute}:{second}")
    if trgt_char in str(hour) or trgt_char in str(minute) or trgt_char in str(second):
        count += 1
print(count)
