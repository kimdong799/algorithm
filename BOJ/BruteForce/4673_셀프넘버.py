numbers = set(range(1, 10000))
remove_set = set()

for i in numbers:
    for j in str(i):
        i += int(j)
    if i <= 10000:
        remove_set.add(i)

self_num = numbers - remove_set

[print(i) for i in sorted(self_num)]