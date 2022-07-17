import sys
def prime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i==0:
                return False
        return True

t=int(sys.stdin.readline())

for i in range(t):
    n=int(sys.stdin.readline())
    a=n//2
    b=a
    while a>0:
        if prime(a) and prime(b):
            print(a,b)
            break
        else:
            a-=1
            b+=1