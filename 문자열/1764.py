from collections import Counter
n,m=map(int,input().split(' '))
d=[]
b=[]
for i in range(n):
    name1=str(input().rstrip())
    d.append(name1)
for j in range(m):
    name2=str(input().rstrip())
    b.append(name2)
rst=d+b
result=Counter(rst)
dab=[]
for key, value in result.items():
    if value>=2:
        dab.append(key)
dab.sort()
print(len(dab))
for i in dab:
    print(i)