import sys
n,m=map(int,sys.stdin.readline().split(' '))
height=list(map(int,sys.stdin.readline().split(' ')))
start=0
end=max(height)
while start<=end:
    rst=0
    mid=(start+end)//2
    for x in height:
        if x>mid:
            rst+=x-mid
    if rst>=m:
        start=mid+1
    else:
        end=mid-1
print(end)