import sys,math
a,b,c=map(int,sys.stdin.readline().rstrip().split(' '))
if(b >= c):
    print(-1)

else:

    re=(a/(c-b))
    print((int(re))+1)