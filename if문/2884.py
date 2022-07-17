h,m=map(int,input().split(' '))
if(h>24 or h<0 or m>60 or m<0):
    exit()
if(m>=45):
    m=m-45
elif(m<45):
    m=m+15
    h=h-1
    if(h<0):
        h=h+24
print(h,m, sep=' ')