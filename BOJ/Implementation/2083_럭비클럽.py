members = []

while True:
    member = input()
    if member == "# 0 0":
        break
    members.append(member)

for member in members:
    name, age, weight = member.split()[0], member.split()[1], member.split()[2]
    if int(age) > 17 or int(weight) >= 80:
        result = name + " Senior"
    else:
        result = name + " Junior"
    print(result) 