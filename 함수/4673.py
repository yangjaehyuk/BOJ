m=set()
n=set(range(1,10001))
for i in range(1,10001):
    n=str(i)
    int_n=list(map(int,n))
    if(len(int_n)<2):
        result1=int_n[0]+int_n[len(int_n)-1]
    else:
        result1=sum(int_n)+int(n)
    m.add(result1)

for i in range(1,10001):
    if(i in m):
        pass
    else:
        print(i)




