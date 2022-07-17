import sys
a=int(sys.stdin.readline().rstrip())
i=1
while a>i:
    a-=i
    i+=1

if i%2==0:
    bunja=a
    bunmo=i-a+1
else:
    bunja=i-a+1
    bunmo=a
print(bunja,'/',bunmo,sep='')