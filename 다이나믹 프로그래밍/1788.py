import sys
n=int(sys.stdin.readline())
if(n<0 and n%2==0):
    print(-1)
elif(n==0):
    print(0)
else:
    print(1)
n=abs(n)
if(n==0):
    print(0)
    exit()
elif(n==1):
    print(1)
    exit()
dp=[0]*(n+1)
dp[0]=0
dp[1]=1
dp[2]=1
for i in range(3,n+1):
    dp[i]=(dp[i-2]+dp[i-1])%1000000000
print(dp[n])