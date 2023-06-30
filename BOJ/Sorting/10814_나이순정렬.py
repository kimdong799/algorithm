import sys

n = int(sys.stdin.readline())

class User:
    def __init__(self, age, name):
        self.age = int(age)
        self.name = name

users = []
for i in range(n):
    age, name = sys.stdin.readline().strip().split()
    user = User(age, name)
    users.append(user)
users.sort(key=lambda x: x.age)

[print(f"{user.age} {user.name}") for user in users]