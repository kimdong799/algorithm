def selfNumber(x):
    if x >= 10000:
        return
    else:
        print(x)
        x_str = str(x)
        for i in x_str:
            x += int(i)
        selfNumber(x)

x = 1

selfNumber(x)