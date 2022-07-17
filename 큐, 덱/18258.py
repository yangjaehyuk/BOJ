import sys
from collections import deque
n=int(sys.stdin.readline())
rst=deque([])
for i in range(n):
    b=sys.stdin.readline().rstrip()
    if('push' in b):
      rst.append(b[5:])
    elif('pop' in b):
        if(len(rst)==0):
            sys.stdout.write(str(-1)+'\n')
        else:
            sys.stdout.write(str(rst[0])+'\n')
            del(rst[0])
    elif('size' in b):
        sys.stdout.write(str(len(rst))+'\n')
    elif('empty' in b):
        if(len(rst)==0):
            sys.stdout.write(str(1)+'\n')
        else:
            sys.stdout.write(str(0)+'\n')
    elif('front' in b):
        if(len(rst)==0):
            sys.stdout.write(str(-1)+'\n')
        else:
            sys.stdout.write(str(rst[0])+'\n')
    elif('back' in b):
        if(len(rst)==0):
            sys.stdout.write(str(-1)+'\n')
        else:
            sys.stdout.write(str(rst[-1])+'\n')