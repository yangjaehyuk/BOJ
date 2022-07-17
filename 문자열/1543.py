import sys
a=str(sys.stdin.readline().rstrip())
check=str(sys.stdin.readline().rstrip())
count=0
i=0
while i<=len(a)-len(check):
    if a[i:i+len(check)]==check:
        count+=1
        i+=len(check)
    else:
        i+=1
print(count)