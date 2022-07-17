import sys
from collections import deque
t=int(input())
for i in range(t):
    n,m=list(map(int,sys.stdin.readline().split(' ')))
    rst=deque(map(int,sys.stdin.readline().split(' ')))
    real=[0 for i in range(n)]
    real[m]='target'
    r=0
    while True:
        max_rst=max(rst)
        if(rst[0]==max_rst):
            r+=1
            if(real[0]=='target'):
                print(r)
                break
            else:
                rst.popleft()
                real.pop(0)
        else:
            rst.append(rst.popleft())
            real.append(real.pop(0))