n=int(input())
length=list(map(int,input().split(' ')))
price=list(map(int,input().split(' ')))
ans=0
ans+=length[0]*price[0]
mini=price[0]
for i in range(1,n-1):
    if price[i]<mini:
        mini=price[i]
    ans+=length[i]*mini
print(ans)