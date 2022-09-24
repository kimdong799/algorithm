a = '_.-;;-._'
b = "'-..-'"
c = '   ||   '

n = 5

for i in range(n):
    if i==0:
        print('       ' + a)
    elif i == n-1:
        a = a.replace(';', "'")
        print(b+'|'+a+'|')
    else:
        if i % 2 == 0:
            print(b+'|'+a+'|')
        else:
            print(b+'|'+c+'|')
    
