import sys
import math
num=int(sys.stdin.readline())
for _ in range(num):
    a=list(map(int,sys.stdin.readline().split(' ')))
    x=a[0]
    y=a[1]
    dist=y-x
    k=0
    rst=0
    while True:
        if(dist==1):
            rst=1
        k+=1
        if(dist-pow(k,2)<=0):
            break
        elif(dist-pow(k,2)<=k):
            rst=2*k
        else:
            rst=2*k+1
    print(rst)