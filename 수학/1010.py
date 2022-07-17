from math import comb
t=int(input())
for i in range(t):
    rst=[]
    n,m=list(map(int,input().split(' ')))
    rst=comb(m,n)
    print(rst)