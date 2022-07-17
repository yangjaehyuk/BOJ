import sys
n=int(sys.stdin.readline())
rst=[]
p='+'
m='-'
c=0
stack=[]
for i in range(n):
    a=int(sys.stdin.readline())
    while c<a:
        c+=1
        stack.append(c)
        rst.append(p)
    if stack[-1]==a:
        stack.pop()
        rst.append(m)
    else:
        stack=False
        break
if(stack==False):
    print("NO")
else:
    for j in rst:
        print(j)