a=list(input())
k=[]
for i in range(0,len(a)):
    k.append(a[i])
tmp1=a[0]
tmp2=a[2]
a[2]=tmp1
a[0]=tmp2

tmp3=a[4]
tmp4=a[6]
a[6]=tmp3
a[4]=tmp4

if(a[0:3]>a[4:7]):
    s=''.join(a)
    print(s[0:3])
else:
    s=''.join(a)
    print(s[4:7])
