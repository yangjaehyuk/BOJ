import sys
a,b=list(map(str,sys.stdin.readline().rstrip().split(' ')))
a=list(a)
b=list(b)
scount=0
rst=[]
for i in range(len(b)):
    if(len(a)==len(b)):
        if(a[i]!=b[i]):
            scount+=1
    else:
        dcount=0
        """a[0:len(a)],b[i:len(a)+i]"""
        A=a[0:len(a)]
        B=b[i:len(a)+i]
        for j in range(len(A)):
            if(A[j]!=B[j]):
                dcount+=1
        rst.append(dcount)
        if(len(a)+i==len(b)):
            break
if(len(a)==len(b)):
    print(scount)
else:
    print(min(rst))