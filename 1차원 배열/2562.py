num=[]
for i in range(9):
    n=int(input())
    num.append(n)
max=max(num)
print(max)
index=num.index(max)
print(index+1)
