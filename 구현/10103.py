n=int(input())
csum=ssum=100
for i in range(n):
    c,s=list(map(int,input().split(' ')))
    if(c<s):
        csum-=s
    elif(c>s):
        ssum-=c
    else:
        continue
print(csum)
print(ssum)