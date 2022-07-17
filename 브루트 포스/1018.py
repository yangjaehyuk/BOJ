a,b=map(int,input().split(' '))
d=[]
W='WBWBWBWB'
B='BWBWBWBW'
p=[W,B,W,B,W,B,W,B]
q=[B,W,B,W,B,W,B,W]
for i in range(0,a):
    d.append((input()))
r=float('inf')
for j in range(a-8+1):
    for k in range(b-8+1):
        c=0
        for l in range(8):
            for m in range(8):
                if(d[j+l][k+m]!=p[l][m]):
                    c+=1
        r=min(r,c)
        c=0
        for l in range(8):
            for m in range(8):
                if(d[j+l][k+m]!=q[l][m]):
                    c+=1
        r=min(r,c)

print(r)
