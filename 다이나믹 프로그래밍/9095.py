import sys
t=int(sys.stdin.readline())
def hab(n):
    if(n==1):
        return 1
    elif(n==2):
        return 2
    elif(n==3):
        return 4
    else:
        return hab(n-1)+hab(n-2)+hab(n-3)
for i in range(t):
    n=int(sys.stdin.readline())
    print(hab(n))