import sys

T = int(sys.stdin.readline())

fileList = []
for i in range(0, T):
    fileName = sys.stdin.readline().rstrip()
    fileList.append(list(fileName))
    
for i in range(len(fileList)):
    for j in range(len(fileList[i])):
        if i == 0:
            continue
        else:
            if fileList[i][j] == fileList[i-1][j]:
                continue
            elif fileList[i-1][j] == "?":
                fileList[i][j] = "?"
            else:
                fileList[i][j] = "?"
            
print("".join(fileList[-1]))