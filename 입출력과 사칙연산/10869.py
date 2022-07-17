a,b=map(int,input().split(' '))
if(a<1 or a>10000 or b<1 or b>10000 ):
    exit()
result1=a+b
result2=a-b
result3=a*b
result4=int(a/b)
result5=a%b
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
