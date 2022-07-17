n,k=map(int,input().split(' '))
dp=[[0]*_ for _ in range(1,n*k+1)]
for i in range(0,n*k):
    for j in range(i+1):
        if j==0:
            dp[i][j]=1
        elif j==i:
            dp[i][j]=1
        else:
            dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
print(dp[n-1][k-1])