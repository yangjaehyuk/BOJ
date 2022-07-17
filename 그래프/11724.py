import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split(' '))
graph = [[] for _ in range(n + 1)]
for i in range(m):
    start,end=list(map(int,sys.stdin.readline().split(' ')))
    graph[start].append(end)
    graph[end].append(start)
visit=[0]*(n+1)
def bfs(v):
    q=[v]
    while q:
        v=q.pop(0)
        for i in graph[v]:
            if visit[i]==0:
                q.append(i)
                visit[i]=1
count=0
for i in range(1,n+1):
    if visit[i]==0:
        bfs(i)
        count+=1
print(count)