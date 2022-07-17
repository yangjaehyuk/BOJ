import sys
n=int(sys.stdin.readline())
num=list(sys.stdin.readline().lower())
sum=0
for i in range(n):
    rst1=ord(num[i])-96
    rst=rst1*(31**i)
    sum+=rst
print(sum%1234567891)