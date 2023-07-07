import sys

input_list = []

while True:
    input_value = sys.stdin.readline().strip()
    if input_value == "0":
        break
    else:
        input_list.append(input_value)

for input_value in input_list:
    split_value = list(input_value)
    if split_value == split_value[::-1]:
        print("yes")
    else:
        print("no")