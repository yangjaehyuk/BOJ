a,b=map(int,input().split(' '))
if(a<-10000 or a>10000 or b<-10000 or b>10000):
    exit()
if(a>b):
    print('>')
if(a<b):
    print('<')
if(a==b):
    print('==')