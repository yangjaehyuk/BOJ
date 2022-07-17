import sys
t=int(sys.stdin.readline())
def cn0(n):
    c0=[1,0]
    for j in range(2, n+1):
        c0.append(c0[j-1]+c0[j-2])
    return c0[n]
def cn1(n):
    c1=[0,1]
    for j in range(2, n+1):
        c1.append(c1[j-1]+c1[j-2])
    return c1[n]

for i in range(t):
    n=int(sys.stdin.readline())
    print(cn0(n),cn1(n))