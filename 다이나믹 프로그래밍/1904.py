import sys
n=int(sys.stdin.readline())
dp=[0]*n
def su(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        dp[0]=1
        dp[1]=2
        for i in range(2,n):
            dp[i]=(dp[i-1]+dp[i-2])%15746
    return dp[-1]
rst=su(n)
print(rst%15746)