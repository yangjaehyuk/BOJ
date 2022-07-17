'''from itertools import permutations
n=list(input())
a=list(itertools.permutations(n,len(n)))
c=[]
for i in range(len(a)):
    b="".join(a[i])
    b=int(b)
    if(b%3==0 and b%10==0):
        c.append(b)
if len(c)!=0:
    print(max(c))
else:
    print(-1)'''
n=input()
ans=[]
if(int(n)%3==0 and int(n)%10==0):
    print(n)
elif(sum(list(map(int,n)))%3==0):
    n=list(map(int,n))
    n.sort(reverse=True)
    b=n[-1]
    if b==0:
        c="".join(map(str,n))
        print(int(c))
    else:
        print(-1)
else:
    print(-1)