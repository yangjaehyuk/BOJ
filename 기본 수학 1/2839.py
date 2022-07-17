import sys
num=int(sys.stdin.readline())
rst=0
while rst*3<=num:
    q,r=divmod(num-rst*3, 5)
    if not r:
        break
    else:
        rst+=1
else:
    print(-1)
    exit()
print(q+rst)