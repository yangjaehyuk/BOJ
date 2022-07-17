a = str(input().lower().split())
b = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in b:
    a=(a.replace(i,'a'))
print(len(a[2:len(a)-2]))