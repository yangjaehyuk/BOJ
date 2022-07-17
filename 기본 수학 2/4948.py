import sys
import math
while True:
    a=int(sys.stdin.readline())
    if a==0:
        exit()
    elif a==1:
        print(1)
    else:
        d=a*2
        e=[]
        array = [True for i in range(d+1)]
        for i in range(2, int(math.sqrt(d)) + 1):
            if array[i]==True:
                j=2
                while i*j<=d:
                    array[i*j] = False
                    j+=1
        for i in range(a+1, d+1):
            if array[i]:
                e.append(i)
        print(len(e))