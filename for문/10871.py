n,x=map(int,input().split(' '))
A=list(map(int,input().split(' ')))
for i in range(1):
    for j in range(1):
        for k in range(n):
            if(A[k]<x):
                result=A[k]
                print(result,end=' ')