import sys
n=int(sys.stdin.readline())
rst=[]
hab=0
a=list(map(int,sys.stdin.readline().split(' ')))
new_a=sorted(a,reverse=False)
for i in range(n):
    hab+=new_a[i]
    rst.append(hab)
print(sum(rst))