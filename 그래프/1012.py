import sys
from collections import deque

t = int(sys.stdin.readline())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q=deque()

def bfs(x, y):
    bae[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if bae[nx][ny] == 1:
                bfs(nx, ny)


for i in range(t):
    m, n, k = map(int, sys.stdin.readline().split(' '))
    bae = [[0 for col in range(n)] for row in range(m)]
    cnt = 0
    for j in range(k):
        x, y = map(int, sys.stdin.readline().split(' '))
        for X in range(m):
            for Y in range(n):
                bae[x][y] = 1
    for i in range(m):
        for j in range(n):
            if bae[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)
