import sys
from collections import deque
n=int(sys.stdin.readline())
rst=[]
deq=deque(rst)
for i in range(1,n+1):
    deq.append(i)
for j in range(len(deq)):
    if(len(deq)>1):
        deq.popleft()
        deq.append(deq[0])
        deq.popleft()
    else:
        print(deq[0])