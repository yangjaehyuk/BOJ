a=int(input())
b=int(input())
c=int(input())
result=a*b*c
d=list(map(int,str(result)))

for i in range(0,10):
    print(d.count(i))