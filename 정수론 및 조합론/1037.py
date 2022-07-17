n=int(input())
a=list(map(int,input().split(' ')))
for i in range(len(a)):
    min_a=min(a)
    max_a=max(a)
    rst=min_a*max_a
print(rst)