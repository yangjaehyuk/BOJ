import sys
a=int(sys.stdin.readline())
b=[]
for i in range(a):
    c=str(sys.stdin.readline().rstrip())
    b.append(c)
new_b=list(set(b))
new_b.sort()
new_b.sort(key=len)
for i in new_b:
    print(i)