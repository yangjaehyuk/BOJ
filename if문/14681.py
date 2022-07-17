a=int(input())
b=int(input())
if(a>1000 or a<-1000 or b>1000 or b<-1000):
    exit()
if(a>0 and b>0):
    print('1')
elif(a<0 and b>0):
    print('2')
elif(a<0 and b<0):
    print('3')
else:
    print('4')