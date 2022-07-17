'''
a=int(input())
b=int(input())
c=[]
d=[]
e=[]
f=[]
for i in range(a,b+1):
    c.append(i)
for j in range(0,b-a+1):
    for k in range(1, c[j] + 1):
        if(c[j]%k==0):
            e.append(c[j])
    if(e.count(c[j])==2):
        f.append(c[j])
if len(f)>0:
    su=sum(f)
    min=min(f)
    print(su)
    print(min)
else:
    print(-1)
에라토스테네스의 체'''
import math
a=int(input())
b=int(input())
d = []
n = b
array = [True for i in range(n + 1)]


for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:

        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1


for i in range(a, n + 1):
    if array[i]:
        d.append(i)
if 1 in d:
    d.remove(1)

if(len(d)>0):
    sum=sum(d)
    min=min(d)
    print(sum)
    print(min)
else:
    print(-1)