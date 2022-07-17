n=int(input())
for i in range(1,n+1):
    b=list(map(int,input().split(' ')))
    print(min(b),max(b), end=" ")
    break