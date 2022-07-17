import sys
m=int(sys.stdin.readline())
s=[]
for i in range(m):
    a=sys.stdin.readline().rstrip()
    if("add" in a):
        if(int(a[4:]) not in s):
            s.append(int(a[4:]))
        else:
            continue
    elif("check" in a):
        if(int(a[6:]) in s):
            sys.stdout.write(str(1)+"\n")
        elif(int(a[6:] not in s)):
            sys.stdout.write(str(0)+"\n")
    elif("remove" in a):
        if(int(a[7:]) in s):
            x=int(a[7:])
            s.remove(x)
        elif(int(a[7:]) not in s):
            continue
    elif("toggle" in a):
        if(int(a[7:]) not in s):
            s.append(int(a[7:]))
        elif(int(a[7:]) in s):
            x=int(a[7:])
            s.remove(x)

    elif('all' in a):
        s.clear()
        s=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    elif("empty" in a):
        s.clear()