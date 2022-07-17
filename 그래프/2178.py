import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split(' '))
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(m)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q=deque()
def bfs(x,y):
    q.append([x,y])
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if graph[nx][ny] == 1:
                    graph[nx][ny]=graph[x][y]+1
                    q.append([nx,ny])
    return graph[m-1][n-1]
print(bfs(0,0))