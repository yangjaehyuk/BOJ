from collections import Counter
n=int(input())
for i in range(n):
    r=[]
    dab=1
    m=int(input())
    for j in range(m):
        a=(list(map(str,input().rstrip().split(' '))))
        r.append(a[1])
    b=Counter(r)
    for key, value in b.items():
        dab*=(value+1)
    print(dab-1)