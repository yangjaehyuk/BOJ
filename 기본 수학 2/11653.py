num=int(input())
for i in range(2,num+1):
    while(num%int(i)==0):
        print(i)
        num/=i