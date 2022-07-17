n=int(input())
c=0
for i in range(n):
    a=input()
    c+=list(a)==sorted(a, key=a.find)
print(c)