string = input()

[print(i.lower(), end='') if i.isupper() else print(i.upper(), end='') for i in string]