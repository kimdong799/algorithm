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