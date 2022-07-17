rst=[0 for i in range(200)]
rst[0]=1
rst[1]=1
rst[2]=1
n=int(input())
if(n==1):
    print(rst[0])
elif(n==2):
    print(rst[1])
elif(n==3):
    print(rst[2])
else:
    for i in range(3,n):
        rst[i]=(rst[i-1]+rst[i-3])

    print(max(rst))