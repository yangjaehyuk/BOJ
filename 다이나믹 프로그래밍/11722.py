import sys
n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split(' ')))
ra=a[::-1]
dp=[1]*n
for i in range(n):
    for j in range(i):
        if(ra[i]>ra[j]):
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))