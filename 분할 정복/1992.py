n=int(input())
paper=[list(map(int,input())) for _ in range(n)]
rst=[]
def make(x,y,n):
    color=paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color!=paper[i][j]:
                rst.append("(")
                make(x,y,n//2)
                """1사분면"""
                make(x,y+n//2,n//2)
                """2사분면"""
                make(x+n//2,y,n//2)
                """3사분면"""
                make(x+n//2,y+n//2,n//2)
                rst.append(")")
                return
    if color==0:
        rst.append(0)
    else:
        rst.append(1)
make(0,0,n)
for i in rst:
    print(i,end='')