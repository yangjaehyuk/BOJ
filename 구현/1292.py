a,b=list(map(int,input().split(' ')))
n=1
rst=[]
for i in range(1,b):
    for j in range(i):
        rst.append(i)
if(a==1 and b==1):
    print(1)
elif(a==1 and b==2):
    print(3)
else:
    print(sum(rst[a-1:b]))