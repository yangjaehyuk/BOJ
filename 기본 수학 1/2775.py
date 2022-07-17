import sys
num=int(sys.stdin.readline())
for i in range(num):
    a=1
    k=int(sys.stdin.readline())
    n=int(sys.stdin.readline())
    array = [[1 for col in range(n)] for row in range(k+1)]
    for l in range(k+1):
        for j in range(n):
            array[l][0]=1
            array[l][j]=array[l-1][j]+array[l][j-1]
    if(n==1):
        for m in range(k+1):
            array[m][0]=1
        print(1)
    else:
        print(array[k][n - 1])
