import sys
t=int(sys.stdin.readline())
for _ in range(t):
    a,b=(map(int,sys.stdin.readline().split(' ')))
    rst=a*b
    if(b>a):
        a,b=b,a
    while(b!=0):
        a=a%b
        a,b=b,a
    print(int(rst/a))