import math
while True:
    n=list(map(int,input().split(' ')))
    if(n[0]==0 and n[1]==0 and n[2]==0):
        break
    max_n=max(n[0],n[1],n[2])
    if(n[0]==max_n):
        n[0]=n[2]
        n[2]=max_n
    if (n[1] == max_n):
        n[1] = n[2]
        n[2] = max_n
    if (n[2] == max_n):
        n[2] = max_n
    if not (n[0]==0 and n[1]==0 and n[2]==0):
        if(pow(n[0],2)+pow(n[1],2)==pow(max_n,2)):
            print('right')
        else:
            print('wrong')