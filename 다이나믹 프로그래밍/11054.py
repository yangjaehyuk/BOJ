import sys
n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split(' ')))
ra=a[::-1]
increase=[1]*n
decrease=[1]*n
for i in range(n):
    for j in range(i):
        if a[i]>a[j]:
            increase[i]=max(increase[i],increase[j]+1)
        if ra[i]>ra[j]:
            decrease[i]=max(decrease[i],decrease[j]+1)
rst=[0]*n
for i in range(n):
    rst[i]=increase[i]+decrease[n-i-1]-1
print(max(rst))