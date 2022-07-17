a=list(map(int,input().split(' ')))
tmp=0
while True:
    if(sorted(a))==a:
        break
    for i in range(0, len(a)-1):
        if (a[i]>a[i+1]):
            tmp=a[i]
            a[i]=a[i+1]
            a[i+1]=tmp
            print(*a)