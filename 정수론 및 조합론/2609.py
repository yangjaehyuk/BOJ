list=list(map(int,input().split(' ')))
a=list[0]
b=list[1]
max_v=max(a,b)
maximum=[]
rst=0
for i in range(1,max_v+1):
    if(a%i==0 and b%i==0):
        maximum.append(i)
    rst=(a//max(maximum))*(b//max(maximum))*max(maximum)
print(max(maximum))
print(rst)