n=int(input())
paper=[list(map(int,input().split(' '))) for _ in range(n)]
rst=[]
def make(x,y,n):
    color=paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color!=paper[i][j]:
                make(x,y,n//3)
                make(x,y+n//3,n//3)
                make(x,y+n//3+n//3,n//3)
                make(x+n//3,y,n//3)
                make(x+n//3,y+n//3,n//3)
                make(x+n//3,y+n//3+n//3,n//3)
                make(x+n//3+n//3,y,n//3)
                make(x+n//3+n//3,y+n//3,n//3)
                make(x+n//3+n//3,y+n//3+n//3,n//3)
                return
    if color==0:
        rst.append(0)
    elif color==1:
        rst.append(1)
    else:
        rst.append(-1)
make(0,0,n)
print(rst.count(-1))
print(rst.count(0))
print(rst.count(1))