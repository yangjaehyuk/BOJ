from math import factorial
n=int(input())
rst=factorial(n)
count=0
r=list(map(int,str(rst)))
for i in reversed(range(len(r))):
    if(r[i]==0):
        count+=1
    elif r[i]!=0:
        break
print(count)