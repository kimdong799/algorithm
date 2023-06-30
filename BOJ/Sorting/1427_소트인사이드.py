import sys

# init num list
num_list = []
result = ''
# input string
input_string = sys.stdin.readline().rstrip()

for i in input_string:
    num_list.append(int(i))

num_list.sort(reverse=True)

for i in num_list:
    result += str(i)
print(result)