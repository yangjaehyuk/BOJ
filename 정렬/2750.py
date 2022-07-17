a=int(input())
c=[]
for i in range(a):
    b=int(input())
    c.append(b)
c=set(c)
new_c=sorted(c,reverse=False)
for j in range(len(new_c)):
    print(new_c[j])