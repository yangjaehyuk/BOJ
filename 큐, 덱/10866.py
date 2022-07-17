import sys
from collections import deque
n=int(sys.stdin.readline())
rst=[]
deq=deque(rst)
for i in range(n):
    b=sys.stdin.readline().rstrip()
    if('push_front' in b):
        deq.appendleft(b[11:])
    elif('push_back' in b):
        deq.append(b[10:])
    elif('pop_front' in b):
        if(len(deq)==0):
            print(-1)
        else:
            print(deq[0])
            deq.popleft()
    elif('pop_back' in b):
        if(len(deq)==0):
            print(-1)
        else:
            print(deq[-1])
            deq.pop()
    elif('size' in b):
        print(len(deq))
    elif('empty' in b):
        if(len(deq)==0):
            print(1)
        else:
            print(0)
    elif('front' in b):
        if(len(deq)==0):
            print(-1)
        else:
            print(deq[0])
    elif('back' in b):
        if(len(deq)==0):
            print(-1)
        else:
            print(deq[-1])
