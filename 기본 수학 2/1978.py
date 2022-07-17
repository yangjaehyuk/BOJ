a=int(input())
b=list(map(int,input().split(' ')))
c=0
d=[]
for i in range(0,len(b)):
    if(b[i]==1):
        c+=0
    else:
        for j in range(1,b[i]+1):
            '''print(b[i],j,b[i]%j)
            print(b.count(b[i]%j==0))'''
            if(b[i]%j==0):
                d.append(b[i])
    if(d.count(b[i])==2):
        c+=1
'''for k in d:
    try: count[k]+=1
    except: count[k]=1'''
print(c)
