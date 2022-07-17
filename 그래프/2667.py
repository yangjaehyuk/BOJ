import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]


def bfs(x, y):
    graph[x][y] = 0
    q = deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 1
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    q.append([nx, ny])
                    cnt += 1
    return cnt


rst = [bfs(i, j) for i in range(n) for j in range(n) if graph[i][j] == 1]
rst.sort()
print(len(rst))
for i in rst:
    print(i)
