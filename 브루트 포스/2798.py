from itertools import permutations
a,b=map(int,input().split(' '))
c=list(map(int,input().split(' ')))
d=[]
e=[]
if(len(c)>a):
    exit()
k=list(permutations(c,3))
for i in range(0,len(k)):
    su=sum(k[i])
    d.append(su)
    if(d[i]<=b):
        e.append(d[i])
print(max(e))