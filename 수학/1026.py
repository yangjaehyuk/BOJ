import sys
n=int(sys.stdin.readline())
sum=0
a=list(map(int,sys.stdin.readline().split(' ')))
new_a=sorted(a,reverse=True)
b=list(map(int,sys.stdin.readline().split(' ')))
new_b=sorted(b,reverse=False)
for i in range(len(new_a)):
    rst=new_a[i]*new_b[i]
    sum+=rst
print(sum)