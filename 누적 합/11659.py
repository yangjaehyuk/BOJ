import sys
n,m=map(int,sys.stdin.readline().split(' '))
k=list(map(int,sys.stdin.readline().split(' ')))
sv=0
prefix_sum=[0]
for i in k:
    sv+=i
    prefix_sum.append(sv)
for j in range(m):
    a,b=map(int,sys.stdin.readline().split(' '))
    print(prefix_sum[b]-prefix_sum[a-1])
