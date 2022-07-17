a=input().split(' ')
b=[]
for i in range(5):
    rst=pow(int(a[i]),2)
    b.append(rst)
su=sum(b)
r=su%10
print(r)