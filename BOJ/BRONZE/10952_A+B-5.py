while True:
    try:
        A, B = map(int, input().split())
        if A==0 and B==0:
            raise Exception("last index")
        print(A+B)
    except:
        break