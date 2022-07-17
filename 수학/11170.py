import sys
t=int(sys.stdin.readline())
for i in range(t):
    n,m=list(map(int,sys.stdin.readline().split(' ')))
    count=0
    for j in range(n,m+1):
        rst=str(j)
        count+=rst.count('0')
    print(count)