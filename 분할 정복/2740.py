n,m=map(int,input().split(' '))
awonso=[]
bwonso=[]
for i in range(n):
    w_1=list(map(int,input().split(' ')))
    awonso.append(w_1)
b,K=map(int,input().split(' '))
for j in range(b):
    w_2=list(map(int,input().split(' ')))
    bwonso.append(w_2)
for i in range(n):
    for j in range(K):
        rst=0
        for k in range(m):
            rst+=awonso[i][k]*bwonso[k][j]
        print(rst, end=' ')
    print()