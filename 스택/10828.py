import sys
n=int(sys.stdin.readline())
rst=[]
for i in range(n):
    b=sys.stdin.readline().rstrip()
    if('push' in b):
        rst.append(b[5:])
    elif('pop' in b):
        if (len(rst)==0):
            print(-1)
        else:
            print(rst[-1])
            del(rst[-1])
    elif('size' in b):
        print(len(rst))
    elif('empty' in b):
        if(len(rst)==0):
            print(1)
        else:
            print(0)
    elif('top' in b):
        if (len(rst) == 0):
            print(-1)
        else:
            print(rst[-1])