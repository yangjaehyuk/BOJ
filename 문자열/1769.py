import sys
count=0
def recursion(val):
    global count
    if (len(val)<2):
        if not (int(val) % 3):
            return 1
        else:
            return 0
    count+=1
    t=0
    for i in val:
        t+=int(i)
    return (recursion(str(t)))

x=sys.stdin.readline().strip()
ans=recursion(x)
print(count)
if (ans):
    print("YES")
else:
    print("NO")