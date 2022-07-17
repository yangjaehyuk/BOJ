n=int(input())
real_result=0
while(n<1 or n>1000000):
    n=int(input())
result=0
i=1
for i in range(n+1):
    n_list=list(map(int,str(i)))
    result=sum(n_list)
    real_result=result+i
    if(n==real_result):
        print(i)
        break
else:
    print('0')