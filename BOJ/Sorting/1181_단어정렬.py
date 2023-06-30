import sys

# init values
input_list = []
length_list = []
result_list = []
# input iteration num
N = int(sys.stdin.readline())

# get input string
for i in range(0, N):
    input_list.append(sys.stdin.readline().rstrip())
print("*INSERT VALUES TO LIST DONE*")

input_list.sort()

for i in input_list:
    length_list.append(len(i))

length_list.sort()
length_list = list(dict.fromkeys(length_list))

for i in length_list:
    for j in input_list:
        if i == len(j):
            result_list.append(j)
            
result_list = list(dict.fromkeys(result_list))

print("----result----")
for i in result_list:
    print(i)
result_list