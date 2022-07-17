n,k=map(int,input().split(' '))
a=n-k
n1=1
k1=1
a1=1
'''rst=n!/k!*a!'''
for i in range(1,n+1):
    n1*=i
for j in range(1,k+1):
    k1*=j
for m in range(1,a+1):
    a1*=m
print(int(n1/(k1*a1)))