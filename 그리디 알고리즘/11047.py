import sys
n,k=map(int,sys.stdin.readline().split(' '))
r=[]
count=0
for i in range(n):
    a=int(sys.stdin.readline())
    r.append(a)
r.sort(reverse=True)
for j in r:
    count+=k//j
    k%=j
print(count)