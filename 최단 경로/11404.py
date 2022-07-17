n=int(input())
m=int(input())
INF=int(1e9)
adj_mat=[[INF]*(n) for _ in range(n)]
for _ in range(m):
    start,end,price=list(map(int,input().split(' ')))
    adj_mat[start-1][end-1]=min(adj_mat[start-1][end-1],price)
for k in range(n):
    for i in range(n):
        for j in range(n):
            if(i==j):
                adj_mat[i][j]=0
            else:
                adj_mat[i][j]=min(adj_mat[i][j],adj_mat[i][k]+adj_mat[k][j])
for row in adj_mat:
    for i in range(n):
        if(row[i]==INF):
            row[i]=0
        print(row[i],end=' ')
    print()