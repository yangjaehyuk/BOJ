rst=[]
for i in range(5):
    a=int(input())
    if(a>=40):
        rst.append(a)
    else:
        rst.append(40)
s=sum(rst)
print(int(s/5))