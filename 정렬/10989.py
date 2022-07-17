import sys
num=int(sys.stdin.readline().rstrip())
v=[0]*10001
for _ in range(num):
    num1=int(sys.stdin.readline().rstrip())
    v[num1]+=1
for i in range(len(v)):
    for j in range(v[i]):
        print(i)