import sys
n,m=map(int,sys.stdin.readline().split(' '))
def cnt2(n):
    count=0
    while n!=0:
        n=n//2
        count+=n
    return count

def cnt5(n):
    count=0
    while n!=0:
        n=n//5
        count+=n
    return count

if(m==0):
    print(0)
else:
    print(min(cnt2(n)-cnt2(m)-cnt2(n-m),cnt5(n)-cnt5(m)-cnt5(n-m)))