import sys

def min_button_press(target_channel, broken_buttons):
    current_channel = 100
    min_press = abs(target_channel - current_channel)

    # 버튼을 눌러서 이동하는 경우
    for channel in range(1000000): # 리모컨은 0~9까지 존재하며 채널은 500,000까지 존재한다. 따라서 6개 숫자를 9로 입력하는 999,999까지 검증
        channel_str = str(channel)

        for digit in channel_str:
            if int(digit) in broken_buttons:
                break
        else:
            min_press = min(min_press, len(channel_str) + abs(target_channel - channel))

    return min_press

# 입력
target_channel = int(sys.stdin.readline())                      # 이동 대상 채널
number_of_broken_buttons = int(sys.stdin.readline())            # 고장난 버튼의 수
if number_of_broken_buttons != 0:
    broken_buttons = list(map(int,sys.stdin.readline().split()))    # 고장난 버튼
else:
    broken_buttons = []

# 결과 출력
result = min_button_press(target_channel, broken_buttons)
print(result)

# import sys
# import itertools

# target_channel = int(sys.stdin.readline())                      # 이동 대상 채널
# number_of_broken_buttons = int(sys.stdin.readline())            # 고장난 버튼의 수
# if number_of_broken_buttons != 0:
#     broken_buttons = list(map(int,sys.stdin.readline().split()))    # 고장난 버튼
# else:
#     broken_buttons = []
# current_channel = 100 # 현재 채널

# usable_buttons = list(range(10)) # 사용 가능한 버튼

# cnt = abs(target_channel - current_channel)  # 채널 이동 횟수

# # 사용 가능한 버튼 리스트 복사 후 수정
# usable_buttons_copy = usable_buttons.copy()
# for button in broken_buttons:
#     usable_buttons_copy.remove(button)


# def find_approximation(target_channel, usable_buttons):
#     min_error = float('inf')
#     best_combination = None

#     for i in range(1, len(list(str(target_channel)))+2):
#         combinations = itertools.product(usable_buttons, repeat=i)
#         for combination in combinations:
#             error = abs(target_channel - int(''.join(map(str, combination))))
#             if error < min_error:
#                 min_error = error
#                 best_combination = combination
#     return int(''.join(map(str, best_combination)))

# if usable_buttons_copy:
#     approximation = find_approximation(target_channel, usable_buttons_copy)
#     cnt = min(cnt, len(str(approximation)) + abs(target_channel - approximation))

# print(cnt)

# print(f"target_channel : {target_channel}")
# print(f"number_of_broken_buttons : {number_of_broken_buttons}")
# print(f"broken buttons : {broken_buttons}")
# print(f"usable buttons : {usable_buttons}")
# print(f"current_channel : {current_channel}")
# print(f"cnt : {cnt}")