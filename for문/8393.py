n=int(input())
result=0
if(n<1 or n>10000):
    exit()
for i in range(n):
    result+=(i-n)
print(abs(result))
