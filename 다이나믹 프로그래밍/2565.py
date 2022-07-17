import sys
n=int(sys.stdin.readline())
line_list=[]
dp=[1]*n
for i in range(n):
    line_list.append(list(map(int,sys.stdin.readline().split(' '))))
line_list.sort(key=lambda x:(x[1],x[0]))
for j in range(n):
    for k in range(j):
        if line_list[j]>line_list[k]:
            dp[j]=max(dp[j],dp[k]+1)
print(n-max(dp))