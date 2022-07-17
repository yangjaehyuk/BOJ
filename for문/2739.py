n=int(input())
if(n<1 or n>9):
    exit()
for i in range(9):
    result=n*(i+1)
    print(n,"*",i+1,"=",result)