import sys
k=int(sys.stdin.readline())
rst=[]
for i in range(k):
    a=int(sys.stdin.readline())
    rst.append(a)

    if(a==0):
        rst.pop()
        rst.pop()
print(sum(rst))