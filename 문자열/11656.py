n=list(input().rstrip())
n=list(n)
rst=[]
while True:
    if(len(n)>0):
        rst.append("".join(n))
        n.pop(0)
    else:
        break
r=sorted(rst,reverse=False)
for i in r:
    print(i)