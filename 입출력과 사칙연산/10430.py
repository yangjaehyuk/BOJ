a,b,c=map(int,input().split(' '))
if(a<2 or a>10000 or b<2 or b>10000 or c<2 or c>10000):
    exit()
result1=(a+b)%c
result2=((a%c)+(b%c))%c
result3=(a*b)%c
result4=((a%c)*(b%c))%c

print(result1)
print(result2)
print(result3)
print(result4)