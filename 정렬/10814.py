import sys
a=int(sys.stdin.readline().rstrip())
c=[]
for i in range(a):
    age,name=input().split(' ')
    age=int(age)
    c.append((age,name))
new_c=sorted(c, key=lambda x:(x[0]),reverse=False)
for i in range(a):
    print(new_c[i][0],new_c[i][1])