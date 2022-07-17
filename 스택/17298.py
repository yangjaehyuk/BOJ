import sys
n=int(sys.stdin.readline())
rst=list(map(int,sys.stdin.readline().split(' ')))
stack=[]
ans=[-1 for _ in range(n)]
for i in range(n):
    while stack and rst[stack[-1]]<rst[i]:
        ans[(stack.pop())]=rst[i]
    stack.append(i)
print(*ans)