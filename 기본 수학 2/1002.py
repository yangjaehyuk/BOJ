import sys
import math
t=int(sys.stdin.readline())
for i in range(t):
    su=list(map(int,sys.stdin.readline().split(' ')))
    x1=su[0]
    y1=su[1]
    r1=su[2]
    x2=su[3]
    y2=su[4]
    r2=su[5]
    distance=math.sqrt((x1-x2)**2+(y1-y2)**2)
    if(distance==0 and r1==r2):
        print(-1)
    elif(abs(r1-r2)==distance or distance==r1+r2):
        print(1)
    elif(abs(r1-r2)<distance<r1+r2):
        print(2)
    else:
        print(0)