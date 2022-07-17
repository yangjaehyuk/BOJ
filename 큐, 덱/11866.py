from collections import deque
n,k=map(int,input().split(' '))
rst=deque([])
ans=[]
for i in range(1,n+1):
    rst.append(i)
print('<',end='')
while rst:
    for j in range(k-1):
        rst.append(rst.popleft())
    print(rst.popleft(),end='')
    if rst:
        print(',',end=' ')
print('>')