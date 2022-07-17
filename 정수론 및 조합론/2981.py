import sys
import math
n=int(sys.stdin.readline())
nlist=[]
rst=[]
r=[]
for i in range(n):
    num=int(sys.stdin.readline())
    nlist.append(num)
nlist.sort()
g=nlist[1]-nlist[0]
for i in range(len(nlist)-1):
    g=math.gcd(nlist[i]-nlist[i+1],g)
    rst.append(g)
gf=int(g**(1/2))
for i in range(2,gf+1):
    if g%i==0:
        r.append(i)
        r.append(g//i)
r.append(g)
r=list(set(r))
r.sort()
print(*r)