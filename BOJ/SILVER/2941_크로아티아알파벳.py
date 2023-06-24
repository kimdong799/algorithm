exception_char_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

for i in exception_char_list:
    word = word.replace(i, "*")
print(len(word))