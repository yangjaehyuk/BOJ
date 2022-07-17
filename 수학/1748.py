import sys
from math import pow
n=int(sys.stdin.readline())
count=0
ln=len(str(n))
for i in range(1,ln):
    count+=i*(pow(10,i)-pow(10,i-1))
count+=ln*(n-pow(10,ln-1)+1)
print(int(count))