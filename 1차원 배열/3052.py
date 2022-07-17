a=0
b=[]
c=[]
set_list=[]
count=1
for i in range(0,10):
    a=int(input())
    b.append(a)
    result=b[i]%42
    c.append(result)
    set_list=set(c)
print(len(set_list))