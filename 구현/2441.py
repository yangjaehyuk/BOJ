n=int(input())
k=0
for i in reversed(range(n+1)):
    print(' '*k,end='')
    print('*'*i)
    k+=1